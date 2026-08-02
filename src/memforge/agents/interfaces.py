from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Sequence

from memforge.models.belief import Belief
from memforge.agora.result import AgentResult

@dataclass(slots=True, frozen=True)
class AgentMetaData:

     identifier: str
     codename:str
     alias:str

     category:str
     domain:str

     version:str
     author:str

     description:str

     priority:int

     enabled_by_default: bool

     tags: list[str]

class EvaluationAgent(Protocol):

    @property
    def metadata(self) -> AgentMetaData: ...
    def supports(self,belief:Belief) -> bool: ...
    def evaluate(self, belief:Belief) -> AgentResult: ...
    def reset(self) ->None: ...        