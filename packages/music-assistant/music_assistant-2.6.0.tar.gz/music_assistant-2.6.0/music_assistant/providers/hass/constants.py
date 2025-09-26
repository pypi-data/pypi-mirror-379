"""Constants for the Home Assistant provider."""

from __future__ import annotations

from enum import IntFlag

from music_assistant_models.enums import PlayerState


class MediaPlayerEntityFeature(IntFlag):
    """Supported features of the media player entity."""

    PAUSE = 1
    SEEK = 2
    VOLUME_SET = 4
    VOLUME_MUTE = 8
    PREVIOUS_TRACK = 16
    NEXT_TRACK = 32

    TURN_ON = 128
    TURN_OFF = 256
    PLAY_MEDIA = 512
    VOLUME_STEP = 1024
    SELECT_SOURCE = 2048
    STOP = 4096
    CLEAR_PLAYLIST = 8192
    PLAY = 16384
    SHUFFLE_SET = 32768
    SELECT_SOUND_MODE = 65536
    BROWSE_MEDIA = 131072
    REPEAT_SET = 262144
    GROUPING = 524288
    MEDIA_ANNOUNCE = 1048576
    MEDIA_ENQUEUE = 2097152


StateMap = {
    "playing": PlayerState.PLAYING,
    "paused": PlayerState.PAUSED,
    "buffering": PlayerState.PLAYING,
    "idle": PlayerState.IDLE,
    "off": PlayerState.IDLE,
    "standby": PlayerState.IDLE,
    "unknown": PlayerState.IDLE,
    "unavailable": PlayerState.IDLE,
}

# HA states that we consider as "powered off"
OFF_STATES = ("unavailable", "unknown", "standby", "off")
UNAVAILABLE_STATES = ("unavailable", "unknown")
