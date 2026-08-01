from datetime import datetime, timezone
from agora.result   import AgentResult
from agora.vote import Vote

class ChronosAgent:

    def __init__(self, name: str = "Chronos" ):
       self.name = name    

    def evaluate(self, belief, reference_time: datetime = None) -> AgentResult :
        ref_time = reference_time or datetime.now(timezone.utc)

        belief_time =  belief.created_at

        if belief_time.tzinfo is None:
            belief_time =  belief_time.replace(tzinfo=timezone.utc)
        if ref_time.tzinfo is None:
            ref_time =  ref_time.replace(tzinfo=timezone.utc)

        age_days = (ref_time - belief_time).days

        if age_days < 0:
            age_days = 0

        if age_days < 30:
            score = 0.90
            vote = Vote.ACCEPT
            reason = f"Fresh information ({age_days} days old)"     

        elif age_days <= 365:
            score = 0.65
            vote = Vote.NEUTRAL
            reason = f"Moderately fresh information ({age_days} daysa old)"

        else:
            score = 0.30
            vote = Vote.REJECT
            reason = f"Outdated/stale information({age_days} days old)"    

        return AgentResult(
            agent=self.name,
            vote=vote,
            score=score,
            reason=reason 
        )    