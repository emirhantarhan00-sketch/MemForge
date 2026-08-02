from __future__ import annotations
from memforge.agents.interfaces import(
    AgentMetaData,
    EvaluationAgent,
)
from memforge.agora.result import AgentResult
from memforge.agora.vote import Vote
from memforge.models.belief import Belief

class Veritas(EvaluationAgent):
    @property

    def metadata(self) -> AgentMetaData:
        return AgentMetaData (
            identifier="veritas",
            codename="Veritas" ,
             alias = "Reliable",
            category="Evaluation",
            domain="Reliability",
            version="0.1.0" ,         
            author="MemForge",
            description="Evaluates epistemic confidence of beliefs.",
            priority=100,
            tags=["belief", "confidence", "trust"],
            enabled_by_default=True,
    )    
    def supports(self, belief:Belief) ->bool:
        return True

    def evaluate(self,belief:Belief) -> AgentResult:
        evidence_count = len(belief.evidences)
        score = self._calculate_score(evidence_count)
        vote = self._generate_vote(score)
        reason = self._generate_reason(
            evidence_count,
            score,
        )

        return AgentResult(
           agent=self.metadata.codename,
           score=score,
           vote=vote,
           reason=reason,
        )

    def reset(self) -> None:
       return None

    def _calculate_score(self, evidence_count: int) -> float:

       if evidence_count >= 5:
          return 0.90

       if evidence_count>=2:
          return 0.65

       return 0.30

    def _generate_vote(self, score: float) -> Vote:

       if score >= 0.75:
          return Vote.ACCEPT

       if score >= 0.40:
          return Vote.NEUTRAL

       return Vote.REJECT

    def _generate_reason(
          self,
          evidence_count: int,
          score: float,
    ) -> str:

       return(
          f"Evaluated using {evidence_count} evidence item(s)."
          f"Epistemic confidence: {score:.2f}."
       )
