from __future__ import annotations

from typing import Iterable

from memforge.agents.interfaces import EvaluationAgent
from memforge.models.belief import Belief
from memforge.agora.result import AgentResult


class Council:
    """
    Coordinates evaluation agents inside AGORA.

    Council does not make the final decision.
    It collects evaluations from supported agents.
    """

    def __init__(
        self,
        agents: Iterable[EvaluationAgent] | None = None,
    ) -> None:
        self._agents: list[EvaluationAgent] = list(agents or [])

    def add_agent(self, agent: EvaluationAgent) -> None:
        """Add an evaluation agent to the council."""
        self._agents.append(agent)

    def evaluate(self, belief: Belief) -> list[AgentResult]:
        """
        Ask all supporting agents to evaluate the belief.

        Agents that do not support the belief are skipped.
        """
        results: list[AgentResult] = []

        for agent in self._agents:
            if not agent.supports(belief):
                continue

            result = agent.evaluate(belief)
            results.append(result)

        return results

    def agents(self) -> list[EvaluationAgent]:
        """Return the registered agents."""
        return list(self._agents)

    def __len__(self) -> int:
        return len(self._agents)