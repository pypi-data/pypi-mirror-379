"""Base Webserver logic for an HTTPServer that can handle dynamic routes."""

from __future__ import annotations

from collections.abc import Coroutine
from typing import TYPE_CHECKING, Any, Final

from aiohttp import web

if TYPE_CHECKING:
    import logging
    from collections.abc import Callable

    from aiohttp.typedefs import Handler


MAX_CLIENT_SIZE: Final = 1024**2 * 16
MAX_LINE_SIZE: Final = 24570


class Webserver:
    """Base Webserver logic for an HTTPServer that can handle dynamic routes."""

    def __init__(
        self,
        logger: logging.Logger,
        enable_dynamic_routes: bool = False,
    ) -> None:
        """Initialize instance."""
        self.logger = logger
        # the below gets initialized in async setup
        self._apprunner: web.AppRunner | None = None
        self._webapp: web.Application | None = None
        self._tcp_site: web.TCPSite | None = None
        self._static_routes: list[tuple[str, str, Handler]] | None = None
        self._dynamic_routes: dict[str, Callable] | None = {} if enable_dynamic_routes else None
        self._bind_port: int | None = None
        self._ingress_tcp_site: web.TCPSite | None = None

    async def setup(
        self,
        bind_ip: str | None,
        bind_port: int,
        base_url: str,
        static_routes: list[tuple[str, str, Handler]] | None = None,
        static_content: tuple[str, str, str] | None = None,
        ingress_tcp_site_params: tuple[str, int] | None = None,
    ) -> None:
        """Async initialize of module."""
        self._base_url = base_url.removesuffix("/")
        self._bind_port = bind_port
        self._static_routes = static_routes
        self._webapp = web.Application(
            logger=self.logger,
            client_max_size=MAX_CLIENT_SIZE,
            handler_args={
                "max_line_size": MAX_LINE_SIZE,
                "max_field_size": MAX_LINE_SIZE,
            },
        )
        self._apprunner = web.AppRunner(self._webapp, access_log=None, shutdown_timeout=10)
        # add static routes
        if self._static_routes:
            for method, path, handler in self._static_routes:
                self._webapp.router.add_route(method, path, handler)
        if static_content:
            self._webapp.router.add_static(
                static_content[0], static_content[1], name=static_content[2]
            )
        # register catch-all route to handle dynamic routes (if enabled)
        if self._dynamic_routes is not None:
            self._webapp.router.add_route("*", "/{tail:.*}", self._handle_catch_all)
        await self._apprunner.setup()
        # set host to None to bind to all addresses on both IPv4 and IPv6
        host = None if bind_ip == "0.0.0.0" else bind_ip
        try:
            self._tcp_site = web.TCPSite(self._apprunner, host=host, port=bind_port)
            await self._tcp_site.start()
        except OSError:
            if host is None:
                raise
            # the configured interface is not available, retry on all interfaces
            self.logger.error(
                "Could not bind to %s, will start on all interfaces as fallback!", host
            )
            self._tcp_site = web.TCPSite(self._apprunner, host=None, port=bind_port)
            await self._tcp_site.start()
        # start additional ingress TCP site if configured
        # this is only used if we're running in the context of an HA add-on
        # which proxies our frontend and api through ingress
        if ingress_tcp_site_params:
            self._ingress_tcp_site = web.TCPSite(
                self._apprunner,
                host=ingress_tcp_site_params[0],
                port=ingress_tcp_site_params[1],
            )
            await self._ingress_tcp_site.start()

    async def close(self) -> None:
        """Cleanup on exit."""
        # stop/clean webserver
        if self._tcp_site:
            await self._tcp_site.stop()
        if self._ingress_tcp_site:
            await self._ingress_tcp_site.stop()
        if self._apprunner:
            await self._apprunner.cleanup()
        if self._webapp:
            await self._webapp.shutdown()
            await self._webapp.cleanup()

    @property
    def base_url(self) -> str:
        """Return the base URL of this webserver."""
        return self._base_url

    @property
    def port(self) -> int | None:
        """Return the port of this webserver."""
        return self._bind_port

    def register_dynamic_route(
        self,
        path: str,
        handler: Callable[[web.Request], Coroutine[Any, Any, web.Response | web.StreamResponse]],
        method: str = "*",
    ) -> Callable:
        """Register a dynamic route on the webserver, returns handler to unregister."""
        if self._dynamic_routes is None:
            msg = "Dynamic routes are not enabled"
            raise RuntimeError(msg)
        key = f"{method}.{path}"
        if key in self._dynamic_routes:
            msg = f"Route {path} already registered."
            raise RuntimeError(msg)
        self._dynamic_routes[key] = handler

        def _remove():
            assert self._dynamic_routes is not None  # for type checking
            return self._dynamic_routes.pop(key)

        return _remove

    def unregister_dynamic_route(self, path: str, method: str = "*") -> None:
        """Unregister a dynamic route from the webserver."""
        if self._dynamic_routes is None:
            msg = "Dynamic routes are not enabled"
            raise RuntimeError(msg)
        key = f"{method}.{path}"
        self._dynamic_routes.pop(key, None)

    async def serve_static(self, file_path: str, request: web.Request) -> web.FileResponse:
        """Serve file response."""
        headers = {"Cache-Control": "no-cache"}
        return web.FileResponse(file_path, headers=headers)

    async def _handle_catch_all(self, request: web.Request) -> web.Response:
        """Redirect request to correct destination."""
        # find handler for the request
        # Try exact match first
        for key in (f"{request.method}.{request.path}", f"*.{request.path}"):
            assert self._dynamic_routes is not None  # for type checking
            if handler := self._dynamic_routes.get(key):
                return await handler(request)
        # Try prefix match (for routes registered with /*)
        if self._dynamic_routes is not None:
            for route_key, handler in self._dynamic_routes.items():
                method, path = route_key.split(".", 1)
                if method in (request.method, "*") and path.endswith("/*"):
                    prefix = path[:-2]
                    if request.path.startswith(prefix):
                        return await handler(request)
        # deny all other requests
        self.logger.warning(
            "Received unhandled %s request to %s from %s\nheaders: %s\n",
            request.method,
            request.path,
            request.remote,
            request.headers,
        )
        return web.Response(status=404)
