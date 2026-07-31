from __future__ import  annotations
from dataclasses import dataclass, field
from memforge.models.evidence import Evidence
@dataclass(slots=True)
class Belief:
    evidences: list[Evidence] = field(default_factory=list)