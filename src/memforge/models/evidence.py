from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import uuid4

class EvidenceType(str, Enum):
    SUPPORTING = "supporting"
    CONTRADICTING =  "contradicting"

@dataclass(slots=True)
class Evidence:

    claim_id: str
    observation_id: str
    evidance_type: EvidanceType

    id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def __post_init__(self) -> None:
        if not self.claim_id.strip():
           raise ValueError("Evidence must be linked to a claim")
        if not self.observation_id.strip():
          raise ValueError("Evidence must be linked to an observation_id")