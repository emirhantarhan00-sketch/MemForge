import pytest 
from memforge.models import ObservationSource, EvidenceType
from memforge.noema import ObservationEngine, ClaimEngine, EvidenceEngine

def test_observation_engine_creation():
    engine = ObservationEngine()
    obs = engine.capture(
        raw_content= "STM32 mikrodenetleyici calisiyorum.",
        source= ObservationSource.USER,
    )
    assert obs.id is not None
    assert obs.raw_content == "STM32 mikrodenetleyici calisiyorum."
    source= ObservationSource.USER

    def test_observation_empty_content_raises_error():
        engine = ObservationEngine()
        with pytest.raises(ValueError, match="raw_content can not be empty."):
            engine.capture(raw_content=" ", source=ObservationSource.USER)

    def test_claim_engine_propose():
        obs_engine = ObservationEngine()
        claim_engine = ClaimEngine()

        obs = obs_engine.capture(
            raw_content= "STM32 C++ kutuphanesi derledim.",
            source= ObservationSource.USER,
        )        
        claim = claim_engine.propose(
            content="Kullanici C++ ile gomulu yazilim gelistiriyor.",
            observations=[obs],  
        )
        assert claim.id is not None
        assert claim.content == "Kullanici C++ ile gomulu yazilim gelistiriyor."
        assert obs.id in claim.observation_ids

    def  test_evidance_engine_evaluation():
        obs_engine = ObservationEngine()
        claim_engine = ClaimEngine()
        evidence_engine = EvidenceEngine()

        obs1 = obs_engine.capture(
            raw_content="STM32 C++ projem derlendi.",
            source=ObservationSource.USER
        )
        claim = claim_engine.propose(
            content="Kullanici C++ biliyor.",
            observations=[obs1],
        )

        obs2 = obs_engine.capture(
            raw_content="Bugun STM32 icin C++ sablon sinifi yazdim.",
            source=ObservationSource.USER,
        )
        evidence = evidence_engine.evaluate(
            claim=claim,
            observation=obs2,
            evidence_type=EvidenceType.SUPPORTING,
        )

        assert evidence.id is not None
        assert evidence.claim_id == claim.id
        assert evidence.observation_id == obs2.id
        assert evidence.evidence_type == EvidenceType.SUPPORTING

        def test_claim_engine_propose():
            from memforge.noema import ObservationEngine, ClaimEngine
            from memforge.models  import ObservationSource

            obs_engine = ClaimEngine()
            claim = claim_engine.propose(observation=obs)

            assert claim.id is not None
            assert "STM32 calisiyorum." in claim.content 
             