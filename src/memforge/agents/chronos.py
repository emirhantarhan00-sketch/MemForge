from datetime import datetime, timezone

from memforge.agora.result import AgentResult
from memforge.agora.vote import Vote
from memforge.agents.interfaces import AgentMetaData


class ChronosAgent:

    _metadata = AgentMetaData(
        identifier="memforge.agent.chronos",
        codename="Chronos",
        alias="Temporal",
        category="Temporal",
        domain="Temporal Relevance",
        version="0.1.1",
        author="MemForge",
        description="Evaluates the temporal relevance and freshness of a belief.",
        priority=80,
        enabled_by_default=True,
        tags=[
            "time",
            "temporal",
            "freshness",
            "recency",
        ],
    )

    def __init__(
        self,
        name: str = "Chronos",
    ):
        self.name = name

    @property
    def metadata(self) -> AgentMetaData:
        return self._metadata

    def supports(self, belief) -> bool:
        return hasattr(
            belief,
            "created_at",
        )

    def evaluate(
        self,
        belief,
        reference_time: datetime = None,
    ) -> AgentResult:

        ref_time = (
            reference_time
            or datetime.now(timezone.utc)
        )

        belief_time = belief.created_at

        if belief_time.tzinfo is None:
            belief_time = belief_time.replace(
                tzinfo=timezone.utc
            )

        if ref_time.tzinfo is None:
            ref_time = ref_time.replace(
                tzinfo=timezone.utc
            )

        age_days = (
            ref_time - belief_time
        ).days

        if age_days < 0:
            age_days = 0

        if age_days < 30:

            score = 0.90
            vote = Vote.ACCEPT

            reason = (
                f"Fresh information "
                f"({age_days} days old)"
            )

        elif age_days <= 365:

            score = 0.65
            vote = Vote.NEUTRAL

            reason = (
                f"Moderately fresh information "
                f"({age_days} days old)"
            )

        else:

            score = 0.30
            vote = Vote.REJECT

            reason = (
                f"Outdated/stale information "
                f"({age_days} days old)"
            )

        return AgentResult(
            agent=self.name,
            vote=vote,
            score=score,
            reason=reason,
        )

    def reset(self) -> None:
        return None