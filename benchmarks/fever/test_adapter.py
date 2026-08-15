import json
from benchmarks.fever.adapter import fever_to_claim

with open(
    "benchmarks/fever/shared_task_dev.jsonl",
    encoding="utf-8"
) as f:
    record = json.loads(f.readline())
    result = fever_to_claim(record)

    print("ID:", result["id"])
    print("Claim:", result["claim"])
    print("Ground truth:", result["ground_truth"])
    print("Verifiable:", result["verifiable"])
    print("Evidence:", result["evidence"])