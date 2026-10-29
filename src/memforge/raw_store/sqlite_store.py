import json
import sqlite3
from datetime import datetime
from pathlib import Path

from memforge.models.observation import Observation, ObservationSource

class SQLiteRawDataStore:
    def __init__(self, db_path: str | Path = "memforge_raw.db"):
        self.db_path = str(db_path)
        self._initialize_database()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _initialize_database(self):
        with self._connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS observations(
                id TEXT PRIMARY KEY,
                source TEXT NOT NULL,
                raw_content TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                context TEXT NOT NULL
                )
                """
            )
    def save(self, observation: Observation) -> str:
        with self._connect() as connection:
            connection.execute(
                """
                INSERT OR REPLACE INTO observations
                (id, source, raw_content, timestamp, context)
                VALUES (?,?,?,?,?)
                """,
                (
                    observation.id,
                    (
                    observation.source.value
                    if isinstance(observation.source, ObservationSource)
                    else observation.source
                    ),
                    observation.raw_content,
                    observation.timestamp.isoformat(),
                    json.dumps(observation.context),
                ),
            )
        return observation.id
    def get(self, observation_id: str) -> Observation | None:
        with sqlite3.connect(self.db_path) as connection:
            row = connection.execute(
                """
                SELECT id, source, raw_content, timestamp, context
                FROM observations
                WHERE id = ?
                """,
                (observation_id,),
            ).fetchone()
        if row is None:
            return None

        return self._deserialize(row)
    @staticmethod
    def _deserialize(row):
        source_value = row[1]

        try:
            source = ObservationSource(source_value)
        except ValueError:
            source = source_value
        return Observation(
            id=row[0],
            source=source,
            raw_content=row[2],
            timestamp=datetime.fromisoformat(row[3]),
            context=json.loads(row[4]),
        )
    def query(
        self,
        *,
        source: str | ObservationSource | None = None,
        parameter_id: str | None = None,
    ) -> list[Observation]:
        sql = """
            SELECT id , source, raw_content, timestamp, context
            FROM observations
        """
        parameters = []

        if source is not None:
            source_value=(
                source.value if isinstance (source, ObservationSource)
                else source
            )
            sql += "WHERE source = ?"
            parameters.append(source_value)

        with self._connect() as connection:
            rows = connection.execute(sql, parameters).fetchall()

        observations = [self._deserialize(row) for row in rows]

        if parameter_id is not None:
            observations = [
                obs for obs in observations
                if obs.context.get("parameter_id") == parameter_id
            ]
            return observations

        @staticmethod
        def _deserialize(row) -> Observation:
            return Observation(
                id=row[0],
                source=ObservationSource(row[1]),
                raw_content=row[2],
                timestamp=datetime.fromisoformat(row[3]),
                context=json.loads(row[4]),
            )