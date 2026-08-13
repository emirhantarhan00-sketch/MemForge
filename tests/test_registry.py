import pytest

from memforge.agents.chronos import ChronosAgent
from memforge.agents.mnemos import Mnemos
from memforge.agents.skepsis import Skepsis
from memforge.agents.veritas import Veritas

from memforge.agora.registry import AgentrRegistry


@pytest.fixture
def registry():
    return AgentrRegistry()


@pytest.fixture
def chronos():
    return ChronosAgent()


@pytest.fixture
def veritas():
    return Veritas()


@pytest.fixture
def mnemos():
    return Mnemos()


@pytest.fixture
def skepsis():
    return Skepsis()


def test_registry_creation(
    registry,
):

    assert len(registry) == 0


def test_register_agent(
    registry,
    chronos,
):

    registry.register(
        chronos,
    )

    assert len(registry) == 1

    assert (
        chronos.metadata.identifier
        in registry
    )


def test_register_multiple_agents(
    registry,
    chronos,
    veritas,
    mnemos,
    skepsis,
):

    registry.register(
        chronos,
    )

    registry.register(
        veritas,
    )

    registry.register(
        mnemos,
    )

    registry.register(
        skepsis,
    )

    assert len(registry) == 4


def test_duplicate_registration(
    registry,
    chronos,
):

    registry.register(
        chronos,
    )

    with pytest.raises(
        ValueError,
    ):

        registry.register(
            chronos,
        )


def test_get_agent(
    registry,
    chronos,
):

    registry.register(
        chronos,
    )

    identifier = (
        chronos.metadata.identifier
    )

    result = registry.get(
        identifier,
    )

    assert result is chronos


def test_get_unknown_agent(
    registry,
):

    with pytest.raises(
        KeyError,
    ):

        registry.get(
            "unknown.agent",
        )


def test_unregister_agent(
    registry,
    chronos,
):

    identifier = (
        chronos.metadata.identifier
    )

    registry.register(
        chronos,
    )

    assert (
        identifier
        in registry
    )

    registry.unregister(
        identifier,
    )

    assert (
        identifier
        not in registry
    )

    assert len(registry) == 0


def test_unregister_unknown_agent(
    registry,
):

    with pytest.raises(
        KeyError,
    ):

        registry.unregister(
            "unknown.agent",
        )


def test_all_agents(
    registry,
    chronos,
    veritas,
    mnemos,
    skepsis,
):

    registry.register(
        chronos,
    )

    registry.register(
        veritas,
    )

    registry.register(
        mnemos,
    )

    registry.register(
        skepsis,
    )

    agents = registry.all_agents()

    assert isinstance(
        agents,
        list,
    )

    assert len(agents) == 4

    assert chronos in agents
    assert veritas in agents
    assert mnemos in agents
    assert skepsis in agents


def test_enabled_agents(
    registry,
    chronos,
    veritas,
    mnemos,
    skepsis,
):

    registry.register(
        chronos,
    )

    registry.register(
        veritas,
    )

    registry.register(
        mnemos,
    )

    registry.register(
        skepsis,
    )

    agents = registry.enabled_agents()

    assert isinstance(
        agents,
        list,
    )

    assert len(agents) == 4

    for agent in agents:

        assert (
            agent.metadata.enabled_by_default
            is True
        )