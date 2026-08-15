from memforge.agora.result import AgentResult
from memforge.agora.vote import Vote
from memforge.agora.voting import VotingEngine


def test_accept_wins():
    results = [
        AgentResult(
            agent="Veritas",
            score=0.90,
            vote=Vote.ACCEPT,
            reason="Strong evidence.",
        ),
        AgentResult(
            agent="Mnemos",
            score=0.80,
            vote=Vote.ACCEPT,
            reason="Worth remembering.",
        ),
        AgentResult(
            agent="Chronos",
            score=0.90,
            vote=Vote.ACCEPT,
            reason="Fresh information.",
        ),
        AgentResult(
            agent="Skepsis",
            score=0.30,
            vote=Vote.REJECT,
            reason="Insufficient confidence.",
        ),
    ]

    engine = VotingEngine()

    result = engine.vote(results)

    assert result.vote is Vote.ACCEPT
    assert result.accept_weight == 2.60
    assert result.reject_weight == 0.30


def test_empty_results():
    engine = VotingEngine()

    result = engine.vote([])

    assert result.vote is Vote.NEUTRAL
    assert result.score == 0.0