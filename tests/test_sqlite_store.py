from memforge.raw_store import SQLiteRawDataStore 
from memforge.engines.observation_engine import ObservationEngine

def test_sqlite_data_survives_store_recration(tmp_path):
    db_path = tmp_path / "test_memforge.db"

    engine = ObservationEngine()
    store= SQLiteRawDataStore(db_path)

    observation= engine.capture(
        raw_content= "Packet loss: 8%" ,
        source="telecom_monitor",
        context={
            "parameter_id": "packet_loss",
            "value": 8.0,
            "unit": "%",
        },
    )
    store.save(observation)

    reopened_store = SQLiteRawDataStore(db_path)
    retrieved= reopened_store.get(observation.id)

    assert retrieved is not None
    assert retrieved.id  == observation.id
    assert retrieved.raw_content == observation.raw_content
    assert retrieved.source == observation.source
    assert retrieved.timestamp == observation.timestamp
    assert retrieved.context == observation.context

    