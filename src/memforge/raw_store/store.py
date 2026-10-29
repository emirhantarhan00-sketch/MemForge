from memforge.models.observation import Observation

class RawDataStore:
    def __init__(self):
        self._records: dict[str, Observation] = {}

    def save(self, observation: Observation) -> str:
        self._records[observation.id] = observation
        return observation.id

    def get(self, observation_id: str) -> Observation | None:
        return self._records.get(observation_id)

    def query(
        self,
        *,
        source: str | None = None,
        parameter_id: str | None=None, 
    ) -> list [Observation]:
        results =  list(self._records.values())

        if source is not None:
            results = [
                obs for obs in results
                if obs.source == source
            ]

        if parameter_id is not None:
            results = [
                 obs for obs in results
                 if obs.context.get("parameter_id") == parameter_id
            ]
            
        return results    