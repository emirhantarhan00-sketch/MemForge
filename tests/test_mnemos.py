from memforge.agents.mnemos import Mnemos
from memforge.models.belief import Belief

def test_mnemos_creation():
    agent = Mnemos()

    assert agent.metadata.codename == "Mnemos"
    assert agent.metadata.alias == "Memory"

    def test_mnemos_evaluate():
        agent = Mnemos

        belief = Belief(
            id="belief-001",
            claim="Python is a programming language."
        )
        result = agent.evaluate(belief)

        assert result.agent =="Mnemos"

        assert result.score >= 0.0
        assert result.score <= 1.0

        assert  result.vote is not None

        assert ininstance(result.reason, str)
        assert len(result.reason) > 0
def test_mnemos_reset():
    agent = Mnemos()

    assert agent.reset() is None