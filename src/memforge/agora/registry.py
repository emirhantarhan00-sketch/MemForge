from __future__ import annotations
from typing import Iterable
from memforge.agents.interfaces import EvaluationAgent

class AgentrRegistry:
    """
    Central Registry from Memforge evaluation Agents.
    The registry is responsible for discovering and managing agents used by AGORA
    """

    def __init__(
            self,
            agents: Iterable[EvaluationAgent] | None = None,
    ) -> None:

        self._agents: dict[str, EvaluationAgent] = {}

        if agents is not None:
            for agent in agents:
                self.register(agent)

    def register(
        self,
        agent: EvaluationAgent,
    ) -> None:
        """
        Register an evaluation AGent
        """ 
        identifier = agent.metadata.identifier

        if identifier in self._agents:
           raise ValueError(
            f"Agent already registered"
        )               
        self._agents[identifier] =  agent
    def unregister(
            self,
            identifier:str,
    ) -> None:

        if identifier not in self._agents:
            raise KeyError(
                f"Agent not found:{identifier}"
            )
        del self._agents[identifier]
    def get(
            self,
            identifier:str,
    ) -> EvaluationAgent:

        try:
            return self._agents[identifier]

        except KeyError:
            raise KeyError (
        f"Agent not found: {identifier}"
            ) from None

    def enabled_agents(
            self,
    ) -> list[EvaluationAgent]:

        return[
            agent 
            for agent in self._agents.values()
            if agent.metadata.enabled_by_default
        ]

    def all_agents(
            self,
    ) ->list[EvaluationAgent]:

        return list(
            self._agents.values()
        )
    def __len__(self) -> int:
        return len(self._agents)

    def __contains__(
            self,
            identifier:str,
    ) -> bool:
        return identifier in self._agents