from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4

@dataclass(slots=True)
class Claim:

    observation_ids: list[str]
    content: str

    id: str = field(default_factory=lambda:str(uuid4))
    timestamp: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )    

    def __post_init__(self) -> None:
        if not self.content.strip():
            raise ValueError("Claim content cannot be empty"  )
        if not self.observation_ids:
            raise ValueError("Claim must be linked to at at least one observation_id")