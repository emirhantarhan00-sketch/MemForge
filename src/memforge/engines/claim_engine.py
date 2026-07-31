import uuid
from typing import Optional
from ..models.claim import Claim

class ClaimEngine:
    def __init__(self, engine_id: str = "default_claim_engine"):
        self.engine_id = engine_id

    def propose(
            self,
            observation,
            content:Optional[str] = None,
            agent_id: Optional[str] = None,
    ) ->Claim:
            claim_text = content or f"Derived claim from:{observation.raw_content}"

            return Claim(
                id=str(uuid.uuid4()),
                content=claim_text
            )
    