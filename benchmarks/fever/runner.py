import json
from pathlib import Path

from memforge.models.belief import Belief
from memforge.models.evidence import Evidence, EvidenceType

from memforge.agora.council import Council

from memforge.agents.skepsis import Skepsis
from memforge.agents.veritas import Veritas
from memforge.agents.mnemos import Mnemos
from memforge.agents.chronos import ChronosAgent
from .results import summarize
from.results import save_results


def fever_to_belief(item: dict) -> Belief:
    """
    Convert one FEVER example into a MemForge Belief.

    Ground-truth label is intentionally NOT passed to MemForge.
    It is only used later by the benchmark evaluator.
    """

    claim_id = str(item["id"])
    claim = item["claim"]

    belief = Belief(
        claim=claim,
        source="FEVER",
        source_type="benchmark",
        confidence=0.5,
        metadata={
            "fever_id": claim_id,
            "ground_truth": item.get("label"),
            "evidence_items": item.get("evidence", []),
        },
    )

    # FEVER evidence is converted into MemForge Evidence objects.
    for index, evidence_item in enumerate(item.get("evidence", [])):

        evidence = Evidence(
            claim_id=claim_id,
            observation_id=f"fever-{claim_id}-observation-{index}",
            evidence_type=EvidenceType.SUPPORTING,
        )

        belief.add_evidence(evidence)

    return belief


def build_council() -> Council:
    """
    Build the AGORA evaluation council.
    """

    agents= [
        Skepsis(),
        Veritas(),
        Mnemos(),
        ChronosAgent(),
    ]
    return Council(agents)


def run_fever(path: str, limit: int | None = None) -> None:

    dataset_path = Path(path)

    council = build_council()

    total = 0

    for line in dataset_path.open("r", encoding="utf-8"):

        if not line.strip():
            continue

        item = json.loads(line)

        belief = fever_to_belief(item)

        results = council.evaluate(belief)

        print("=" * 70)
        print(f"FEVER ID : {item['id']}")
        print(f"CLAIM    : {belief.claim}")
        print(f"EVIDENCE : {belief.evidence_count}")

        for result in results:
            print(
                f"{result.agent:10s} | "
                f"score={result.score:.2f} | "
                f"vote={result.vote.value}"
            )

        total += 1

        if limit is not None and total >= limit:
            break

    print()
    print(f"Processed {total} FEVER examples.")

    save_results(results)


if __name__ == "__main__":
    run_fever(
        "benchmarks/fever/shared_task_dev.jsonl",
        limit=1000,
    )