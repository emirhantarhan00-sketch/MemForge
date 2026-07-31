from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4


class ObservationSource(str, Enum):
    """Represent the origin of an observation."""

    USER = "user"
    SYSTEM = "system"
    SENSOR = "sensor"
    EXTERNAL = "external"


@dataclass(frozen=True, slots=True)
class Observation:
    """Manifesto 2.1: Represents raw input received from a conversation or external source."""

    # 1. Varsayılan değeri olmayan alanlar (Önce gelmeli)
    source: ObservationSource
    raw_content: str

    # 2. Varsayılan değeri olan alanlar (Sonra gelmeli)
    id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    context: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.raw_content.strip():
            raise ValueError("raw_content can not be empty")