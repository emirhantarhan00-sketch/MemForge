from typing import Any, Dict, Optional
from memforge.models.observation import Observation, ObservationSource


class ObservationEngine:
    def capture(
        self,
        raw_content: str,
        source: ObservationSource = ObservationSource.USER,
        context: Optional[Dict[str, Any]] = None,
    ) -> Observation:
        cleaned_content = raw_content.strip()
        return Observation(
            source=source,
            raw_content=cleaned_content,
            context=context or {},
        )