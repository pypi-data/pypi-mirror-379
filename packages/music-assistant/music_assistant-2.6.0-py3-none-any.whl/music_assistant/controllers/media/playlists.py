"""Manage MediaItems of type Playlist."""

from __future__ import annotations

import time
from collections.abc import AsyncGenerator
from typing import Any

from music_assistant_models.enums import MediaType, ProviderFeature
from music_assistant_models.errors import (
    InvalidDataError,
    MediaNotFoundError,
    ProviderUnavailableError,
)
from music_assistant_models.media_items import Playlist, Track

from music_assistant.constants import (
    CACHE_CATEGORY_MUSIC_PLAYLIST_TRACKS,
    CACHE_CATEGORY_MUSIC_PROVIDER_ITEM,
    DB_TABLE_PLAYLISTS,
)
from music_assistant.helpers.compare import create_safe_string
from music_assistant.helpers.json import serialize_to_json
from music_assistant.helpers.uri import create_uri, parse_uri
from music_assistant.models.music_provider import MusicProvider

from .base import MediaControllerBase


class PlaylistController(MediaControllerBase[Playlist]):
    """Controller managing MediaItems of type Playlist."""

    db_table = DB_TABLE_PLAYLISTS
    media_type = MediaType.PLAYLIST
    item_cls = Playlist

    def __init__(self, *args, **kwargs) -> None:
        """Initialize class."""
        super().__init__(*args, **kwargs)
        # register (extra) api handlers
        api_base = self.api_base
        self.mass.register_api_command(f"music/{api_base}/create_playlist", self.create_playlist)
        self.mass.register_api_command("music/playlists/playlist_tracks", self.tracks)
        self.mass.register_api_command(
            "music/playlists/add_playlist_tracks", self.add_playlist_tracks
        )
        self.mass.register_api_command(
            "music/playlists/remove_playlist_tracks", self.remove_playlist_tracks
        )

    async def tracks(
        self,
        item_id: str,
        provider_instance_id_or_domain: str,
        force_refresh: bool = False,
    ) -> AsyncGenerator[Track, None]:
        """Return playlist tracks for the given provider playlist id."""
        playlist = await self.get(
            item_id,
            provider_instance_id_or_domain,
        )
        # a playlist can only have one provider so simply pick the first one
        prov_map = next(x for x in playlist.provider_mappings)
        cache_checksum = playlist.cache_checksum
        # playlist tracks are not stored in the db,
        # we always fetched them (cached) from the provider
        page = 0
        while True:
            tracks = await self._get_provider_playlist_tracks(
                prov_map.item_id,
                prov_map.provider_instance,
                cache_checksum=cache_checksum,
                page=page,
                force_refresh=force_refresh,
            )
            if not tracks:
                break
            for track in tracks:
                yield track
            page += 1

    async def create_playlist(
        self, name: str, provider_instance_or_domain: str | None = None
    ) -> Playlist:
        """Create new playlist."""
        # if provider is omitted, just pick builtin provider
        if provider_instance_or_domain:
            provider = self.mass.get_provider(provider_instance_or_domain)
            if provider is None:
                raise ProviderUnavailableError
        else:
            provider = self.mass.get_provider("builtin")

        # create playlist on the provider
        playlist = await provider.create_playlist(name)
        # add the new playlist to the library
        return await self.add_item_to_library(playlist, False)

    async def add_playlist_tracks(self, db_playlist_id: str | int, uris: list[str]) -> None:
        """Add tracks to playlist."""
        # ruff: noqa: PLR0915
        db_id = int(db_playlist_id)  # ensure integer
        playlist = await self.get_library_item(db_id)
        if not playlist:
            msg = f"Playlist with id {db_id} not found"
            raise MediaNotFoundError(msg)
        if not playlist.is_editable:
            msg = f"Playlist {playlist.name} is not editable"
            raise InvalidDataError(msg)

        # grab all existing track ids in the playlist so we can check for duplicates
        playlist_prov_map = next(iter(playlist.provider_mappings))
        playlist_prov = self.mass.get_provider(playlist_prov_map.provider_instance)
        if not playlist_prov or not playlist_prov.available:
            msg = f"Provider {playlist_prov_map.provider_instance} is not available"
            raise ProviderUnavailableError(msg)
        cur_playlist_track_ids = set()
        cur_playlist_track_uris = set()
        async for item in self.tracks(playlist.item_id, playlist.provider):
            cur_playlist_track_uris.add(item.item_id)
            cur_playlist_track_uris.add(item.uri)

        # unwrap all uri's to track uri's
        unwrapped_uris: list[str] = []
        for uri in uris:
            # URI could be a playlist or album uri, unwrap it
            if not ("://" in uri and len(uri.split("/")) >= 4):
                # NOT a music assistant-style uri (provider://media_type/item_id)
                self.logger.warning(
                    "Not adding %s to playlist %s - not a valid uri", uri, playlist.name
                )
                continue
            # music assistant-style uri
            # provider://media_type/item_id
            provider_instance_id_or_domain, rest = uri.split("://", 1)
            media_type_str, item_id = rest.split("/", 1)
            media_type = MediaType(media_type_str)
            if media_type == MediaType.ALBUM:
                for track in await self.mass.music.albums.tracks(
                    item_id, provider_instance_id_or_domain
                ):
                    unwrapped_uris.append(track.uri)
            elif media_type == MediaType.PLAYLIST:
                for track in await self.tracks(item_id, provider_instance_id_or_domain):
                    unwrapped_uris.append(track.uri)
            elif media_type == MediaType.TRACK:
                unwrapped_uris.append(uri)
            else:
                self.logger.warning(
                    "Not adding %s to playlist %s - not a track", uri, playlist.name
                )
                continue

        # work out the track id's that need to be added
        # filter out duplicates and items that not exist on the provider.
        ids_to_add: set[str] = set()
        for uri in unwrapped_uris:
            # skip if item already in the playlist
            if uri in cur_playlist_track_uris:
                self.logger.info(
                    "Not adding %s to playlist %s - it already exists",
                    uri,
                    playlist.name,
                )
                continue

            # parse uri for further processing
            media_type, provider_instance_id_or_domain, item_id = await parse_uri(uri)

            # skip if item already in the playlist
            if item_id in cur_playlist_track_ids:
                self.logger.warning(
                    "Not adding %s to playlist %s - it already exists",
                    uri,
                    playlist.name,
                )
                continue

            # special: the builtin provider can handle uri's from all providers (with uri as id)
            if provider_instance_id_or_domain != "library" and playlist_prov.domain == "builtin":
                # note: we try not to add library uri's to the builtin playlists
                # so we can survive db rebuilds
                ids_to_add.add(uri)
                self.logger.info(
                    "Adding %s to playlist %s",
                    uri,
                    playlist.name,
                )
                continue

            # if target playlist is an exact provider match, we can add it
            if provider_instance_id_or_domain != "library":
                item_prov = self.mass.get_provider(provider_instance_id_or_domain)
                if not item_prov or not item_prov.available:
                    self.logger.warning(
                        "Skip adding %s to playlist: Provider %s is not available",
                        uri,
                        provider_instance_id_or_domain,
                    )
                    continue
                if item_prov.lookup_key == playlist_prov.lookup_key:
                    ids_to_add.add(item_id)
                    continue

            # ensure we have a full (library) track (including all provider mappings)
            full_track = await self.mass.music.tracks.get(
                item_id,
                provider_instance_id_or_domain,
                recursive=provider_instance_id_or_domain != "library",
            )
            track_prov_domains = {x.provider_domain for x in full_track.provider_mappings}
            if (
                playlist_prov.domain != "builtin"
                and playlist_prov.is_streaming_provider
                and playlist_prov.domain not in track_prov_domains
            ):
                # try to match the track to the playlist provider
                full_track.provider_mappings.update(
                    await self.mass.music.tracks.match_provider(playlist_prov, full_track, False)
                )

            # a track can contain multiple versions on the same provider
            # simply sort by quality and just add the first available version
            for track_version in sorted(
                full_track.provider_mappings, key=lambda x: x.quality, reverse=True
            ):
                if not track_version.available:
                    continue
                if track_version.item_id in cur_playlist_track_ids:
                    break  # already existing in the playlist
                item_prov = self.mass.get_provider(track_version.provider_instance)
                if not item_prov:
                    continue
                track_version_uri = create_uri(
                    MediaType.TRACK,
                    item_prov.lookup_key,
                    track_version.item_id,
                )
                if track_version_uri in cur_playlist_track_uris:
                    self.logger.warning(
                        "Not adding %s to playlist %s - it already exists",
                        full_track.name,
                        playlist.name,
                    )
                    break  # already existing in the playlist
                if playlist_prov.domain == "builtin":
                    # the builtin provider can handle uri's from all providers (with uri as id)
                    ids_to_add.add(track_version_uri)
                    self.logger.info(
                        "Adding %s to playlist %s",
                        full_track.name,
                        playlist.name,
                    )
                    break
                if item_prov.lookup_key == playlist_prov.lookup_key:
                    ids_to_add.add(track_version.item_id)
                    self.logger.info(
                        "Adding %s to playlist %s",
                        full_track.name,
                        playlist.name,
                    )
                    break
            else:
                self.logger.warning(
                    "Can't add %s to playlist %s - it is not available on provider %s",
                    full_track.name,
                    playlist.name,
                    playlist_prov.name,
                )

        if not ids_to_add:
            return

        # actually add the tracks to the playlist on the provider
        await playlist_prov.add_playlist_tracks(playlist_prov_map.item_id, list(ids_to_add))
        # invalidate cache so tracks get refreshed
        playlist.cache_checksum = str(time.time())
        await self.update_item_in_library(db_playlist_id, playlist)

    async def add_playlist_track(self, db_playlist_id: str | int, track_uri: str) -> None:
        """Add (single) track to playlist."""
        await self.add_playlist_tracks(db_playlist_id, [track_uri])

    async def remove_playlist_tracks(
        self, db_playlist_id: str | int, positions_to_remove: tuple[int, ...]
    ) -> None:
        """Remove multiple tracks from playlist."""
        db_id = int(db_playlist_id)  # ensure integer
        playlist = await self.get_library_item(db_id)
        if not playlist:
            msg = f"Playlist with id {db_id} not found"
            raise MediaNotFoundError(msg)
        if not playlist.is_editable:
            msg = f"Playlist {playlist.name} is not editable"
            raise InvalidDataError(msg)
        for prov_mapping in playlist.provider_mappings:
            provider = self.mass.get_provider(prov_mapping.provider_instance)
            if ProviderFeature.PLAYLIST_TRACKS_EDIT not in provider.supported_features:
                self.logger.warning(
                    "Provider %s does not support editing playlists",
                    prov_mapping.provider_domain,
                )
                continue
            await provider.remove_playlist_tracks(prov_mapping.item_id, positions_to_remove)
        # invalidate cache so tracks get refreshed
        playlist.cache_checksum = str(time.time())
        await self.update_item_in_library(db_playlist_id, playlist)

    async def _add_library_item(self, item: Playlist) -> int:
        """Add a new record to the database."""
        db_id = await self.mass.music.database.insert(
            self.db_table,
            {
                "name": item.name,
                "sort_name": item.sort_name,
                "owner": item.owner,
                "is_editable": item.is_editable,
                "favorite": item.favorite,
                "metadata": serialize_to_json(item.metadata),
                "external_ids": serialize_to_json(item.external_ids),
                "cache_checksum": item.cache_checksum,
                "search_name": create_safe_string(item.name, True, True),
                "search_sort_name": create_safe_string(item.sort_name, True, True),
            },
        )
        # update/set provider_mappings table
        await self._set_provider_mappings(db_id, item.provider_mappings)
        self.logger.debug("added %s to database (id: %s)", item.name, db_id)
        return db_id

    async def _update_library_item(
        self, item_id: int, update: Playlist, overwrite: bool = False
    ) -> None:
        """Update existing record in the database."""
        db_id = int(item_id)  # ensure integer
        cur_item = await self.get_library_item(db_id)
        metadata = update.metadata if overwrite else cur_item.metadata.update(update.metadata)
        cur_item.external_ids.update(update.external_ids)
        name = update.name if overwrite else cur_item.name
        sort_name = update.sort_name if overwrite else cur_item.sort_name or update.sort_name
        await self.mass.music.database.update(
            self.db_table,
            {"item_id": db_id},
            {
                # always prefer name/owner from updated item here
                "name": name,
                "sort_name": sort_name,
                "owner": update.owner or cur_item.owner,
                "is_editable": update.is_editable,
                "metadata": serialize_to_json(metadata),
                "external_ids": serialize_to_json(
                    update.external_ids if overwrite else cur_item.external_ids
                ),
                "cache_checksum": update.cache_checksum or cur_item.cache_checksum,
                "search_name": create_safe_string(name, True, True),
                "search_sort_name": create_safe_string(sort_name, True, True),
            },
        )
        # update/set provider_mappings table
        provider_mappings = (
            update.provider_mappings
            if overwrite
            else {*cur_item.provider_mappings, *update.provider_mappings}
        )
        await self._set_provider_mappings(db_id, provider_mappings, overwrite)
        self.logger.debug("updated %s in database: (id %s)", update.name, db_id)

    async def _get_provider_playlist_tracks(
        self,
        item_id: str,
        provider_instance_id_or_domain: str,
        cache_checksum: Any = None,
        page: int = 0,
        force_refresh: bool = False,
    ) -> list[Track]:
        """Return playlist tracks for the given provider playlist id."""
        assert provider_instance_id_or_domain != "library"
        provider: MusicProvider = self.mass.get_provider(provider_instance_id_or_domain)
        if not provider:
            return []
        # prefer cache items (if any)
        cache_category = CACHE_CATEGORY_MUSIC_PLAYLIST_TRACKS
        cache_base_key = provider.lookup_key
        cache_key = f"{item_id}.{page}"
        if (
            not force_refresh
            and (
                cache := await self.mass.cache.get(
                    cache_key,
                    checksum=cache_checksum,
                    category=cache_category,
                    base_key=cache_base_key,
                )
            )
            is not None
        ):
            return [Track.from_dict(x) for x in cache]
        # no items in cache (or force_refresh) - get listing from provider
        items = await provider.get_playlist_tracks(item_id, page=page)
        # store (serializable items) in cache
        self.mass.create_task(
            self.mass.cache.set(
                cache_key,
                [x.to_dict() for x in items],
                checksum=cache_checksum,
                category=cache_category,
                base_key=cache_base_key,
            )
        )
        for item in items:
            # if this is a complete track object, pre-cache it as
            # that will save us an (expensive) lookup later
            if item.image and item.artist_str and item.album and provider.domain != "builtin":
                await self.mass.cache.set(
                    f"track.{item_id}",
                    item.to_dict(),
                    category=CACHE_CATEGORY_MUSIC_PROVIDER_ITEM,
                    base_key=provider.lookup_key,
                )
        return items

    async def radio_mode_base_tracks(
        self,
        item_id: str,
        provider_instance_id_or_domain: str,
    ):
        """Get the list of base tracks from the controller used to calculate the dynamic radio."""
        return [
            x
            async for x in self.tracks(item_id, provider_instance_id_or_domain)
            # filter out unavailable tracks
            if x.available
        ]
