"""Execution helpers for running tiles."""

from __future__ import annotations

import inspect
from collections.abc import Iterator, Mapping, MutableMapping
from contextlib import contextmanager
from typing import Any, TypeVar

from .context import TileContext
from .errors import TileExecutionError, TileRegistrationAggregateError, TileRegistrationError
from .events import EventBus, get_event_bus, reset_event_bus, set_event_bus
from .plugins import TilePluginManager
from .registry import TileRegistry
from .tile import Tile

type TileRef = str | type[Tile[Any, Any]] | Tile[Any, Any]
PayloadT = TypeVar("PayloadT", bound=Any)
ResultT = TypeVar("ResultT", bound=Any)

_default_registry = TileRegistry()
_default_plugins = TilePluginManager()


def get_registry() -> TileRegistry:
    return _default_registry


def get_plugins() -> TilePluginManager:
    return _default_plugins


def _coerce_tile(tile: TileRef, registry: TileRegistry) -> tuple[type[Tile[Any, Any]], Tile[Any, Any]]:
    if isinstance(tile, Tile):
        return type(tile), tile
    if isinstance(tile, str):
        tile_cls = registry.get(tile)
        return tile_cls, tile_cls()
    if inspect.isclass(tile) and issubclass(tile, Tile):
        return tile, tile()
    raise TileRegistrationError.unsupported_reference(tile)


def _prepare_context(
    *,
    tile: Tile[Any, Any],
    event_bus: EventBus,
    services: Mapping[str, Any] | None,
    state: MutableMapping[str, Any] | None,
) -> TileContext:
    ctx = TileContext(event_bus=event_bus, services=services, state=state)
    tile.set_context(ctx)
    return ctx


def _refresh_registry_from_plugins(registry: TileRegistry, plugins: TilePluginManager) -> None:
    candidates: list[type[Tile[Any, Any]]] = []
    errors: list[TileRegistrationError] = []
    seen: set[str] = set()

    for tile_cls in plugins.iter_tiles():
        name = getattr(tile_cls, "name", None)
        if not name:
            errors.append(TileRegistrationError.missing_name(tile_cls))
            continue
        if name in seen:
            errors.append(TileRegistrationError.duplicate(name))
            continue
        if name in registry:
            existing = registry.info(name)
            contribution_source = getattr(tile_cls, "__module__", None)
            if existing.tile_cls is not tile_cls or existing.source != contribution_source:
                errors.append(TileRegistrationError.duplicate(name))
            continue
        if not issubclass(tile_cls, Tile):
            errors.append(TileRegistrationError.not_subclass(tile_cls))
            continue
        candidates.append(tile_cls)
        seen.add(name)

    if errors:
        raise (errors[0] if len(errors) == 1 else TileRegistrationAggregateError(errors))

    for tile_cls in candidates:
        registry.register(tile_cls, source=getattr(tile_cls, "__module__", None))


def _resolve_invocation(
    tile: TileRef,
    payload: Any,
    *,
    registry: TileRegistry | None,
    event_bus: EventBus | None,
    plugins: TilePluginManager | None,
    services: Mapping[str, Any] | None,
    state: MutableMapping[str, Any] | None,
) -> tuple[type[Tile[Any, Any]], Tile[Any, Any], TileContext, EventBus, TilePluginManager]:
    registry = registry or _default_registry
    plugins = plugins or _default_plugins
    _refresh_registry_from_plugins(registry, plugins)
    resolved_bus = event_bus or get_event_bus()
    tile_cls, tile_obj = _coerce_tile(tile, registry)
    ctx = _prepare_context(tile=tile_obj, event_bus=resolved_bus, services=services, state=state)
    return tile_cls, tile_obj, ctx, resolved_bus, plugins


def _start_invocation(
    *,
    tile_cls: type[Tile[Any, Any]],
    tile_obj: Tile[Any, Any],
    payload: Any,
    ctx: TileContext,
    event_bus: EventBus,
    plugins: TilePluginManager,
) -> None:
    event_bus.emit("runtime.started", tile=tile_cls.name, payload=payload, services=ctx.services)
    try:
        plugins.startup(ctx=ctx, tile=tile_obj)
    except Exception:
        event_bus.emit("runtime.stopped", tile=tile_cls.name, payload=payload)
        tile_obj.set_context(None)
        raise
    event_bus.emit("tile.started", tile=tile_cls.name, payload=payload)


def _complete_invocation(
    *,
    tile_cls: type[Tile[Any, Any]],
    tile_obj: Tile[Any, Any],
    payload: Any,
    result: Any,
    ctx: TileContext,
    event_bus: EventBus,
    plugins: TilePluginManager,
) -> Any:
    shutdown_error: Exception | None = None
    try:
        plugins.shutdown(ctx=ctx, tile=tile_obj, error=None)
    except Exception as exc:
        shutdown_error = exc

    if shutdown_error is None:
        event_bus.emit("tile.completed", tile=tile_cls.name, payload=payload, result=result)
        return result

    event_bus.emit(
        "tile.failed",
        tile=tile_cls.name,
        payload=payload,
        error=shutdown_error,
        phase="shutdown",
    )
    raise TileExecutionError(tile_cls.name, payload, shutdown_error) from shutdown_error


def _handle_execution_failure(
    *,
    tile_cls: type[Tile[Any, Any]],
    tile_obj: Tile[Any, Any],
    payload: Any,
    ctx: TileContext,
    event_bus: EventBus,
    plugins: TilePluginManager,
    error: Exception,
) -> None:
    shutdown_error: Exception | None = None
    try:
        plugins.shutdown(ctx=ctx, tile=tile_obj, error=error)
    except Exception as exc:
        shutdown_error = exc

    final_error = shutdown_error or error
    phase = "shutdown" if shutdown_error is not None else "execute"
    event_bus.emit(
        "tile.failed",
        tile=tile_cls.name,
        payload=payload,
        error=final_error,
        phase=phase,
        original_error=error if shutdown_error is not None else None,
    )

    if shutdown_error is not None:
        raise TileExecutionError(tile_cls.name, payload, shutdown_error) from error

    raise TileExecutionError(tile_cls.name, payload, error) from error


def set_registry(registry: TileRegistry) -> None:
    global _default_registry
    _default_registry = registry


def reset_registry() -> None:
    set_registry(TileRegistry())


def set_plugins(plugins: TilePluginManager) -> None:
    global _default_plugins
    _default_plugins = plugins


def reset_plugins() -> None:
    set_plugins(TilePluginManager())


def reset_runtime_defaults() -> None:
    reset_registry()
    reset_plugins()
    reset_event_bus()


@contextmanager
def scoped_runtime(
    *,
    registry: TileRegistry | None = None,
    plugins: TilePluginManager | None = None,
    event_bus: EventBus | None = None,
) -> Iterator[None]:
    previous_registry = get_registry()
    previous_plugins = get_plugins()
    previous_bus = get_event_bus()

    try:
        if registry is not None:
            set_registry(registry)
        if plugins is not None:
            set_plugins(plugins)
        if event_bus is not None:
            set_event_bus(event_bus)
        yield
    finally:
        set_registry(previous_registry)
        set_plugins(previous_plugins)
        set_event_bus(previous_bus)


def _finalize_invocation(
    *,
    tile_cls: type[Tile[Any, Any]],
    tile_obj: Tile[Any, Any],
    payload: Any,
    event_bus: EventBus,
    started: bool,
) -> None:
    if started:
        event_bus.emit("runtime.stopped", tile=tile_cls.name, payload=payload)
    tile_obj.set_context(None)


def invoke_tile(
    tile: TileRef,
    payload: Any,
    *,
    registry: TileRegistry | None = None,
    event_bus: EventBus | None = None,
    plugins: TilePluginManager | None = None,
    services: Mapping[str, Any] | None = None,
    state: MutableMapping[str, Any] | None = None,
    return_context: bool = False,
) -> Any:
    """Execute ``tile`` synchronously and return the result."""

    tile_cls, tile_obj, ctx, resolved_bus, resolved_plugins = _resolve_invocation(
        tile,
        payload,
        registry=registry,
        event_bus=event_bus,
        plugins=plugins,
        services=services,
        state=state,
    )

    started = False
    try:
        _start_invocation(
            tile_cls=tile_cls,
            tile_obj=tile_obj,
            payload=payload,
            ctx=ctx,
            event_bus=resolved_bus,
            plugins=resolved_plugins,
        )
        started = True
        result = tile_obj.execute(payload)
    except TileExecutionError:
        raise
    except Exception as exc:
        _handle_execution_failure(
            tile_cls=tile_cls,
            tile_obj=tile_obj,
            payload=payload,
            ctx=ctx,
            event_bus=resolved_bus,
            plugins=resolved_plugins,
            error=exc,
        )
    else:
        completed = _complete_invocation(
            tile_cls=tile_cls,
            tile_obj=tile_obj,
            payload=payload,
            result=result,
            ctx=ctx,
            event_bus=resolved_bus,
            plugins=resolved_plugins,
        )
        return (completed, ctx) if return_context else completed
    finally:
        _finalize_invocation(
            tile_cls=tile_cls,
            tile_obj=tile_obj,
            payload=payload,
            event_bus=resolved_bus,
            started=started,
        )


async def ainvoke_tile(
    tile: TileRef,
    payload: Any,
    *,
    registry: TileRegistry | None = None,
    event_bus: EventBus | None = None,
    plugins: TilePluginManager | None = None,
    services: Mapping[str, Any] | None = None,
    state: MutableMapping[str, Any] | None = None,
    return_context: bool = False,
) -> Any:
    """Async counterpart to :func:`invoke_tile`."""

    tile_cls, tile_obj, ctx, resolved_bus, resolved_plugins = _resolve_invocation(
        tile,
        payload,
        registry=registry,
        event_bus=event_bus,
        plugins=plugins,
        services=services,
        state=state,
    )

    started = False
    try:
        _start_invocation(
            tile_cls=tile_cls,
            tile_obj=tile_obj,
            payload=payload,
            ctx=ctx,
            event_bus=resolved_bus,
            plugins=resolved_plugins,
        )
        started = True
        result = await tile_obj.aexecute(payload)
    except TileExecutionError:
        raise
    except Exception as exc:
        _handle_execution_failure(
            tile_cls=tile_cls,
            tile_obj=tile_obj,
            payload=payload,
            ctx=ctx,
            event_bus=resolved_bus,
            plugins=resolved_plugins,
            error=exc,
        )
    else:
        completed = _complete_invocation(
            tile_cls=tile_cls,
            tile_obj=tile_obj,
            payload=payload,
            result=result,
            ctx=ctx,
            event_bus=resolved_bus,
            plugins=resolved_plugins,
        )
        return (completed, ctx) if return_context else completed
    finally:
        _finalize_invocation(
            tile_cls=tile_cls,
            tile_obj=tile_obj,
            payload=payload,
            event_bus=resolved_bus,
            started=started,
        )
