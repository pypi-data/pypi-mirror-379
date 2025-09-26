from __future__ import annotations

import json
from typing import Any, Mapping

from .models import Aggregate, Indicators


def _to_mapping(data: Any) -> Mapping[str, Any]:
    if isinstance(data, (bytes, bytearray)):
        return json.loads(data.decode())
    if isinstance(data, str):
        return json.loads(data)
    if isinstance(data, Mapping):
        return data
    raise TypeError("Unsupported input type for parse function")


def parse_aggregate(data: Any) -> Aggregate:
    obj = _to_mapping(data)
    return Aggregate.from_dict(obj)


def parse_indicators(data: Any) -> Indicators:
    obj = _to_mapping(data)
    return Indicators.from_dict(obj)


