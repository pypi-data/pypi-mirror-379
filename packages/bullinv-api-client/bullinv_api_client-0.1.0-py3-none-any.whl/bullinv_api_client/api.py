from __future__ import annotations

import asyncio
import json
from typing import AsyncIterator, Iterable, Literal

from .models import Aggregate, Indicators
from .ws_client import Subscription, WSClientConfig, WebSocketStream


Endpoint = Literal["aggregates", "indicators"]


def _make_url(base_ws_url: str, endpoint: Endpoint) -> str:
    base = base_ws_url.rstrip("/")
    return f"{base}/{endpoint}"


async def stream(
    base_ws_url: str,
    endpoint: Endpoint,
    subscriptions: Iterable[Subscription] | None = None,
    *,
    max_queue_size: int = 1000,
    drops_before_close: int = 100,
) -> AsyncIterator[dict]:
    config = WSClientConfig(
        url=_make_url(base_ws_url, endpoint),
        max_queue_size=max_queue_size,
        drops_before_close=drops_before_close,
    )
    stream = WebSocketStream(config)
    await stream.connect()
    try:
        if subscriptions:
            await stream.subscribe(list(subscriptions))
        async for raw in stream.messages():
            yield json.loads(raw.decode())
    finally:
        await stream.close()


async def stream_aggregates(
    base_ws_url: str = "ws://localhost:8080",
    subscriptions: Iterable[Subscription] | None = None,
    **kwargs,
) -> AsyncIterator[Aggregate]:
    async for obj in stream(base_ws_url, "aggregates", subscriptions, **kwargs):
        yield Aggregate.from_dict(obj)


async def stream_indicators(
    base_ws_url: str = "ws://localhost:8080",
    subscriptions: Iterable[Subscription] | None = None,
    **kwargs,
) -> AsyncIterator[Indicators]:
    async for obj in stream(base_ws_url, "indicators", subscriptions, **kwargs):
        yield Indicators.from_dict(obj)


