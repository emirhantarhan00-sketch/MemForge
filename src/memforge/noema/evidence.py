from __future__ import annotations

from memforge.models.evidence import Evidance, EvidanceType
from memforge.models.claim import Claim
from memforge.models.observation import Observation

class EvidenceEngine:

   def evaluate (
         self,
         claim: Claim,
         observation: Observation,
         evidence_type: EvidanceType,
   ) -> Evidance:

        return Evidance(
            claim_id=claim.id,
            observation_id=observation.id,
            evidence_type= evidence_type,
        ) 