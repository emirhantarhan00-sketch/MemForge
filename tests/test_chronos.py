from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock
from agents.chronos import ChronosAgent
from agora.vote import Vote

def test_chronos_evaluate_fresh_belief():
    agent = ChronosAgent()
    now = datetime.now(timezone.utc)

    belief = MagicMock()
    belief.created_at = now -timedelta(days=10)

    result = agent.evaluate(belief, reference_time=now)

    assert result.vote == Vote.ACCEPT
    assert result.score == 0.90
    assert "Fresh information" in result.reason

def test_chronos_evaluate_moderate_belief():
    agent = ChronosAgent()
    now = datetime.now(timezone.utc)

    belief = MagicMock()
    belief.created_at = now -timedelta(days=100)   

    result = agent.evaluate(belief, reference_time=now)

    assert result.vote == Vote.NEUTRAL
    assert result.score == 0.65
    assert "Moderately fresh" in result.reason

def test_chronos_evaluate_stale_belief():
    agent = ChronosAgent()
    now = datetime.now(timezone.utc)

    belief = MagicMock
    belief.created_at = now - timedelta(days=400)    

    result = agent.evaluate(belief, reference_time=now)

    assert result.vote == Vote.REJECT
    assert result.score == 0.30
    assert "Outdated/stale" in result.reason