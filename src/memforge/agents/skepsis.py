from __future__ import annotations

from typing import Final

from memforge.agents.interfaces import (
    AgentMetaData,
    EvaluationAgent,
)

from memforge.agora.result import AgentResult
from memforge.agora.vote import Vote
from memforge.models.belief import Belief


class Skepsis(EvaluationAgent):
    """
    Skepsis

    Critical Evaluation Agent

    Unlike the other agents, Skepsis does not try
    to prove a belief.

    Instead it actively searches for weaknesses,
    inconsistencies and possible reasons why the
    belief should NOT be accepted.

    Philosophy
    ----------
    "Extraordinary claims require extraordinary evidence."
    """

    _METADATA: Final = AgentMetaData(
        identifier="memforge.agent.skepsis",
        codename="Skepsis",
        alias="Skeptic",
        category="Critical Evaluation",
        domain="Contradiction Analysis",
        version="0.1.0",
        author="MemForge",
        description=(
            "Attempts to falsify beliefs before "
            "they are accepted by Agora."
        ),
        priority=95,
        enabled_by_default=True,
        tags=(
            "skeptic",
            "critical",
            "reasoning",
            "contradiction",
            "validation",
        ),
    )

    @property
    def metadata(self) -> AgentMetaData:
        return self.__class__._METADATA

    def supports(
        self,
        belief: Belief,
    ) -> bool:
        """
        Skepsis evaluates every belief.
        """
        return True

    def evaluate(
        self,
        belief: Belief,
    ) -> AgentResult:

        evidence_strength = self._calculate_evidence_strength(
            belief,
        )

        source_reliability = self._calculate_source_reliability(
            belief,
        )

        consistency_score = self._calculate_consistency(
            belief,
        )

        contradiction_score = self._calculate_contradiction_score(
            belief,
        )

        extraordinary_score = self._calculate_extraordinary_score(
            belief,
        )

        uncertainty_score = self._calculate_uncertainty(
            belief,
        )

        skepticism_score = self._calculate_skepticism_score(
            evidence_strength,
            source_reliability,
            consistency_score,
            contradiction_score,
            extraordinary_score,
            uncertainty_score,
        )

        confidence = self._calculate_confidence(
            skepticism_score,
        )

        vote = self._generate_vote(
            skepticism_score,
        )

        reason = self._generate_reason(
            evidence_strength,
            source_reliability,
            consistency_score,
            contradiction_score,
            extraordinary_score,
            uncertainty_score,
            skepticism_score,
        )

        return AgentResult(
            agent=self.metadata.codename,
            score=confidence,
            vote=vote,
            reason=reason,
        )

    def reset(self) -> None:
        """
        Skepsis currently stores no runtime state.
        """
        return None

    def _calculate_evidence_strength(
        self,
        belief: Belief,
    ) -> float:

        evidences = getattr(
            belief,
            "evidences",
            [],
        )

        count = len(evidences)

        if count >= 10:
            return 1.0

        if count >= 7:
            return 0.90

        if count >= 5:
            return 0.80

        if count >= 3:
            return 0.65

        if count >= 2:
            return 0.50

        if count == 1:
            return 0.30

        return 0.10


    def _calculate_source_reliability(
        self,
        belief: Belief,
    ) -> float:
        """
        Estimate the reliability of the sources
        supporting this belief.

        v0.1 uses a simple heuristic.
        """

        evidences = getattr(
            belief,
            "evidences",
            [],
        )

        if not evidences:
            return 0.20

        reliability_sum = 0.0

        for evidence in evidences:

            reliability = getattr(
                evidence,
                "reliability",
                0.70,
            )

            reliability_sum += reliability

        return max(
            0.0,
            min(
                1.0,
                reliability_sum / len(evidences),
            ),
        )

    # =====================================================
    # Consistency Analysis
    # =====================================================

    def _calculate_consistency(
        self,
        belief: Belief,
    ) -> float:
        """
        Measures internal consistency.

        v0.1 placeholder implementation.
        """

        claim = getattr(
            belief,
            "claim",
            "",
        )

        if not claim:
            return 0.20

        length = len(str(claim))

        if length > 300:
            return 0.95

        if length > 150:
            return 0.85

        if length > 80:
            return 0.75

        if length > 30:
            return 0.60

        return 0.45

    # =====================================================
    # Contradiction Analysis
    # =====================================================

    def _calculate_contradiction_score(
        self,
        belief: Belief,
    ) -> float:
        """
        Estimate contradiction probability.

        Higher value means fewer contradictions.
        """

        evidence_strength = (
            self._calculate_evidence_strength(
                belief,
            )
        )

        consistency = (
            self._calculate_consistency(
                belief,
            )
        )

        contradiction = (
            evidence_strength * 0.55
            +
            consistency * 0.45
        )

        return max(
            0.0,
            min(
                1.0,
                contradiction,
            ),
        )

    def _calculate_extraordinary_score(
        self,
        belief: Belief,
    ) -> float:
        """
        Higher score means the claim appears
        ordinary and therefore requires less
        extraordinary evidence.

        v0.1 heuristic.
        """

        claim = str(
            getattr(
                belief,
                "claim",
                "",
            )
        ).lower()

        extraordinary_keywords = (
            "always",
            "never",
            "impossible",
            "guaranteed",
            "miracle",
            "magic",
            "100%",
        )

        for keyword in extraordinary_keywords:

            if keyword in claim:
                return 0.35

        return 0.85
        # =====================================================
    # Uncertainty Analysis
    # =====================================================

    def _calculate_uncertainty(
        self,
        belief: Belief,
    ) -> float:
        """
        Estimate uncertainty.

        Higher score means less uncertainty.
        """

        evidence = self._calculate_evidence_strength(
            belief,
        )

        source = self._calculate_source_reliability(
            belief,
        )

        consistency = self._calculate_consistency(
            belief,
        )

        uncertainty = (
            evidence * 0.40
            +
            source * 0.35
            +
            consistency * 0.25
        )

        return max(
            0.0,
            min(
                1.0,
                uncertainty,
            ),
        )

    def _calculate_skepticism_score(
        self,
        evidence_strength: float,
        source_reliability: float,
        consistency_score: float,
        contradiction_score: float,
        extraordinary_score: float,
        uncertainty_score: float,
    ) -> float:
        """
        Overall confidence after skeptical evaluation.
        """

        score = (
            evidence_strength * 0.22
            +
            source_reliability * 0.20
            +
            consistency_score * 0.18
            +
            contradiction_score * 0.20
            +
            extraordinary_score * 0.10
            +
            uncertainty_score * 0.10
        )

        return max(
            0.0,
            min(
                1.0,
                score,
            ),
        )

    # =====================================================
    # Confidence
    # =====================================================

    def _calculate_confidence(
        self,
        skepticism_score: float,
    ) -> float:
        """
        Normalize confidence score.
        """

        return round(
            skepticism_score,
            3,
        )

   
    def _generate_vote(
        self,
        skepticism_score: float,
    ) -> Vote:

        if skepticism_score >= 0.80:
            return Vote.ACCEPT

        if skepticism_score >= 0.50:
            return Vote.NEUTRAL

        return Vote.REJECT
        # =====================================================
    # Reason Generation
    # =====================================================

    def _generate_reason(
        self,
        evidence_strength: float,
        source_reliability: float,
        consistency_score: float,
        contradiction_score: float,
        extraordinary_score: float,
        uncertainty_score: float,
        skepticism_score: float,
    ) -> str:
        """
        Generate a human-readable explanation
        describing Skepsis' decision.
        """

        observations: list[str] = []

        if evidence_strength < 0.50:
            observations.append(
                "Limited supporting evidence was detected."
            )
        else:
            observations.append(
                "Evidence quantity is considered sufficient."
            )

        if source_reliability < 0.60:
            observations.append(
                "Source reliability appears questionable."
            )
        else:
            observations.append(
                "Sources appear reasonably reliable."
            )

        if consistency_score < 0.60:
            observations.append(
                "The belief may contain internal inconsistencies."
            )
        else:
            observations.append(
                "Internal consistency is acceptable."
            )

        if contradiction_score < 0.60:
            observations.append(
                "Possible contradictions require further investigation."
            )
        else:
            observations.append(
                "No major contradictions were detected."
            )

        if extraordinary_score < 0.50:
            observations.append(
                "This appears to be an extraordinary claim."
            )

        if uncertainty_score < 0.50:
            observations.append(
                "Overall uncertainty remains relatively high."
            )

        observations.append(
            f"Final Skepsis confidence: {skepticism_score:.2f}"
        )

        return " ".join(observations)


    def summarize(
        self,
        belief: Belief,
    ) -> dict[str, float]:
        """
        Returns all Skepsis metrics.
        Useful for debugging and future
        Agora visualizations.
        """

        evidence = self._calculate_evidence_strength(
            belief,
        )

        source = self._calculate_source_reliability(
            belief,
        )

        consistency = self._calculate_consistency(
            belief,
        )

        contradiction = self._calculate_contradiction_score(
            belief,
        )

        extraordinary = self._calculate_extraordinary_score(
            belief,
        )

        uncertainty = self._calculate_uncertainty(
            belief,
        )

        confidence = self._calculate_skepticism_score(
            evidence,
            source,
            consistency,
            contradiction,
            extraordinary,
            uncertainty,
        )

        return {
            "evidence_strength": evidence,
            "source_reliability": source,
            "consistency": consistency,
            "contradiction": contradiction,
            "extraordinary": extraordinary,
            "uncertainty": uncertainty,
            "confidence": confidence,
        }