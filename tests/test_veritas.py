import pytest
from unittest.mock import MagicMock

from memforge.agents.veritas import Veritas
from memforge.agora.vote import Vote
from memforge.agora.result import AgentResult

@pytest.fixture
def veritas_agent():

    return Veritas()

@pytest.fixture
def mock_belief():

    def _create_belief(evidences_count: int = 0):
        belief =  MagicMock()
        belief.evidences = [f"evidence_{i}" for i in range(evidences_count)]
        return belief
    return _create_belief

    def test_veritas_metadata(veritas_agent):
        meta = veritas_agent.metadata
        assert meta.codename == "Veritas"
        assert meta.alias == "Reliable"
        assert meta.category == "Evaluation"
        assert meta.domain == "Reliability"
        assert meta.priority == 100
        assert "confidence" in meta .tags

def test_veritas_evaluate_high_evidence_accept(veritas_agent, mock_belief):
    belief = mock_belief(5)        
    result = veritas_agent.evaluate(belief)

    assert isinstance(result, AgentResult)
    assert result.agent == "Veritas"
    assert result.score == 0.90
    assert result.vote == Vote.ACCEPT
    assert "5 evidence item(s)" in result.reason

def test_veritas_evaluate_medium_evidence_neutral(veritas_agent, mock_belief):
    belief = mock_belief(3)    
    result = veritas_agent.evaluate(belief)

    assert result.score == 0.65
    assert result.vote == Vote.NEUTRAL
    assert "3 evidence item(s)" in result.reason

def test_veritas_reset(veritas_agent):
    assert veritas_agent.reset() is None    