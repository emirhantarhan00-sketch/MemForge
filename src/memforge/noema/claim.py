from __future__ import annotations

from memforge.models.claim import Claim
from memforge.models.observation import Observation

class ClaimEngine:
    @classmethod
    def  propose(self,content: str, observation, list[Observation]) -> Claim:
        obs_ids = [obs.id for obs in observations]
        return Claim(content= content, observation_ids=obs_ids)