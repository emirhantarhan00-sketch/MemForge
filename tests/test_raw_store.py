from memforge.raw_store import RawDataStore
from memforge.engines.observation_engine import ObservationEngine

def test_raw_data_store():
    engine  = ObservationEngine()
    store = RawDataStore()

    observation = engine.capture(
        raw_content="Packet loss: 8%",
        source="telecom_monitor",
        context={
            "parameter_id": "packet_loss",
            "value": 8.0,
            "unit": "%",
        },
    )

    saved_id = store.save(observation)
    assert saved_id == observation.id

    retrieved = store.get(saved_id)
    assert retrieved is observation

    results  = store.query(parameter_id="packet_loss")
    assert len(results) == 1
    assert results [0].id == observation.id

    results = store.query(source= "telecom_monitor")
    assert len(results) == 1 

    assert store.get("nonexistent-id") is None