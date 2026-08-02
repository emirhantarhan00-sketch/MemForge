from __future__ import annotations
from memforge.agents.interfaces import(
    AgentMetaData,
    EvaluationAgent,
)
from memforge.agora.result import AgentResult
from memforge.agora.vote import Vote
from memforge.models.belief import Belief

class Mnemos(EvaluationAgent):

    _METADATA = AgentMetaData(
        identifier="memforge.agent.mnemos",
        codename="Mnemos",
        alias="Memory",
        category="Memory",
        domain="Memory Selection",
        version="0.1.1",
        author="MemForge",
        description="Evaluates whether a belief deserves long-term memory.",
        priority=90,
        enabled_by_default=True,
        tags=(
            "memory",
            "importance",
            "novelty",
            "utility",
            "reuse",
        ),
    )
    @property
    def metadata(self) -> AgentMetaData:
        return self.__class__._METADATA
    def supports(self, belief: Belief) -> bool:
        return True
    def evaluate(self, belief:Belief) -> AgentResult:
        novelty = self._calculate_novelty(belief)
        utility = self._calculate_utility(belief)
        persistence = self._calculate_persistence(belief)
        reuse = self._calculate_reuse_prohability(belief)

        memory_worthiness = self._calculate_memory_worthiness(
            novelty,
            persistence,
            reuse,
        )
        vote = self._generate_vote(memory_worthiness)

        reason = self._generate_reason(
            novelty,
            utility,
            persistence,
            reuse,
            memory_worthiness,
        )
        return AgentResult(
            agent=self.metadata.codename,
            score=memory_worthiness,
            vote=vote,
            reason=reason,
        )
    def reset(self) -> None:
        return None

    def _calculate_novelty(
            self,
            belief: Belief,
    ) -> float:

        return 0.80
    def _calculate_utility(
            self,
            belief: Belief,
    ) -> float:

        return 0.75

    def _calculate_persistance(
            self,
            belief: Belief,
    ) -> float:

        return 0.85

    def _calculate_reuse_probability(
            self,
            belief: Belief,
    )  -> float:

        return 0.70

    def _calculate_memory_worthiness(
        self,
        novelty: float,
        utility: float,
        persistance: float,
        reuse: float,
    ) -> float:

        return (
            novelty +
            utility + 
            persistance +
            reuse
        ) /4

    def _generate_vote(
            self,
            score:float,
    ) -> Vote:

        if score >= 0.80:
            return Vote.ACCEPT
        if score >=0.50:
            return Vote.NEUTRAL
        return Vote.REJECT

    def _generate_reason(
            self,
            novelty: float,
            utility: float,
            persistance: float,
            reuse: float,
            score: float,
    ) -> str:
        return(
            f"Novelty={novelty:.2f}, "
            f"Utility{utility:.2f}"
            f"Persistence={persistance:.2f},"
            f"Reuse={reuse:.2f}."
            f"Memory Worthiness={score:.2f}."
        )