from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from memforge.models.evidence import Evidence


@dataclass(slots=True)
class Belief:
    """
    Canonical knowledge representation used throughout MemForge.

    Every agent receives and evaluates Belief objects.
    """

    # --------------------------------------------------
    # Identity
    # --------------------------------------------------

    identifier: str = field(
        default_factory=lambda: str(uuid4())
    )

    # --------------------------------------------------
    # Core proposition
    # --------------------------------------------------

    claim: str = ""

    # --------------------------------------------------
    # Evidence
    # --------------------------------------------------

    evidences: list[Evidence] = field(
        default_factory=list
    )

    # --------------------------------------------------
    # Confidence
    # --------------------------------------------------

    confidence: float = 0.5

    # --------------------------------------------------
    # Source information
    # --------------------------------------------------

    source: str = ""

    source_type: str = "unknown"

    # --------------------------------------------------
    # Metadata
    # --------------------------------------------------

    tags: list[str] = field(
        default_factory=list
    )

    metadata: dict[str, object] = field(
        default_factory=dict
    )

    # --------------------------------------------------
    # Temporal information
    # --------------------------------------------------

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )

    updated_at: datetime = field(
        default_factory=datetime.utcnow
    )

    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------

    active: bool = True

    archived: bool = False

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    access_count: int = 0

    reuse_count: int = 0

    evaluation_count: int = 0

    # --------------------------------------------------
    # Utility
    # --------------------------------------------------

    def add_evidence(
        self,
        evidence: Evidence,
    ) -> None:

        self.evidences.append(evidence)

        self.updated_at = datetime.utcnow()

    def touch(self) -> None:

        self.access_count += 1

        self.updated_at = datetime.utcnow()

    def evaluated(self) -> None:

        self.evaluation_count += 1

        self.updated_at = datetime.utcnow()

    @property
    def evidence_count(self) -> int:

        return len(self.evidences)