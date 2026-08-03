import pytest

from memforge.agents.skepsis import Skepsis
from memforge.models.belief import Belief


@pytest.fixture
def skepsis_agent():
    return Skepsis()


@pytest.fixture
def mock_belief():

    belief = Belief()

    belief.claim = (
        "The Earth revolves around the Sun."
    )

    belief.evidences = [
        object(),
        object(),
        object(),
        object(),
        object(),
    ]

    return belief


def test_skepsis_creation(
    skepsis_agent,
):

    assert (
        skepsis_agent.metadata.codename
        == "Skepsis"
    )


def test_skepsis_supports(
    skepsis_agent,
    mock_belief,
):

    assert (
        skepsis_agent.supports(
            mock_belief,
        )
        is True
    )


def test_skepsis_evaluate(
    skepsis_agent,
    mock_belief,
):

    result = skepsis_agent.evaluate(
        mock_belief,
    )

    assert (
        result.agent
        == "Skepsis"
    )

    assert (
        0.0
        <= result.score
        <= 1.0
    )

    assert (
        result.vote
        is not None
    )

    assert isinstance(
        result.reason,
        str,
    )


def test_skepsis_summary(
    skepsis_agent,
    mock_belief,
):

    summary = skepsis_agent.summarize(
        mock_belief,
    )

    assert isinstance(
        summary,
        dict,
    )

    assert (
        "confidence"
        in summary
    )

    assert (
        "evidence_strength"
        in summary
    )

    assert (
        "source_reliability"
        in summary
    )

    assert (
        "consistency"
        in summary
    )

    assert (
        "contradiction"
        in summary
    )

    assert (
        "extraordinary"
        in summary
    )

    assert (
        "uncertainty"
        in summary
    )


def test_skepsis_reset(
    skepsis_agent,
):

    assert (
        skepsis_agent.reset()
        is None
    )