from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class BeliefMetrics:
 recency: float
 stability:float
 confidence:float
 support_count: int=1
 contradictiion_count: int=0
 created_at: datetime = field(default_factory=datetime.now)

 def to_dict(self) -> dict:
  return{
   "recency":self.recency,
   "stability": self.stability,
   "confidence": self.confidence,
   "support_count": self.support_count,
   "contradiction_count": self.contradictiion_count,
   "created_at": self.created_at.isoformat()
  }