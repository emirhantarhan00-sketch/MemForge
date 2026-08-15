from dataclasses import dataclass
from typing import Iterable

from memforge.agora.result import AgentResult
from memforge.agora.vote import Vote


@dataclass(frozen=True, slots=True)
class VotingResult:
    vote: Vote
    score: float
    accept_weight: float
    neutral_weight: float
    reject_weight: float
    reason: str


class VotingEngine:
    """
    Combines evaluation results from multiple AGORA agents
    into a single collective decision.
    """

    def vote(self, results: Iterable[AgentResult]) -> VotingResult:
        results = list(results)

        if not results:
            return VotingResult(
                vote=Vote.NEUTRAL,
                score=0.0,
                accept_weight=0.0,
                neutral_weight=0.0,
                reject_weight=0.0,
                reason="No agent results were provided.",
            )

        accept_weight = 0.0
        neutral_weight = 0.0
        reject_weight = 0.0

        for result in results:
            weight = max(0.0, min(1.0, result.score))

            if result.vote is Vote.ACCEPT:
                accept_weight += weight

            elif result.vote is Vote.NEUTRAL:
                neutral_weight += weight

            elif result.vote is Vote.REJECT:
                reject_weight += weight

        weights = {
            Vote.ACCEPT: accept_weight,
            Vote.NEUTRAL: neutral_weight,
            Vote.REJECT: reject_weight,
        }

        winning_vote = max(weights, key=weights.get)

        total_weight = (
            accept_weight
            + neutral_weight
            + reject_weight
        )

        if total_weight == 0:
            score = 0.0
        else:
            score = weights[winning_vote] / total_weight

        reason = (
            f"Collective decision based on {len(results)} agent(s). "
            f"Accept={accept_weight:.2f}, "
            f"Neutral={neutral_weight:.2f}, "
            f"Reject={reject_weight:.2f}. "
            f"Winning vote={winning_vote.value}."
        )

        return VotingResult(
            vote=winning_vote,
            score=score,
            accept_weight=accept_weight,
            neutral_weight=neutral_weight,
            reject_weight=reject_weight,
            reason=reason,
        )