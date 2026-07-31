from dataclasses import dataclass
from memforge.agora.vote import Vote

@dataclass(slots=True)
class AgentResult:
   agent: str
   score: float
   vote: Vote
   reason: str