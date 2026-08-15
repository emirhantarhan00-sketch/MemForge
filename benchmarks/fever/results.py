from collections import Counter

def summarize(results):
    total = len(results)

    labels = Counter(
        result["ground_truth"]
        for result in results
    )
    print("DEBUG LABELS:", labels)
    evidence_available = sum(
        1 for result in results
        if result["evidence"]
    )
    evidence_missing = total- evidence_available

    print()
    print("======== MEMFORGE FEVER RESULTS ========")
    print()
    print("Total records           :", total)
    print("Processed           :", total)
    print()
    print("Supports           :", labels["SUPPORTS"])
    print("Refutes         :", labels["REFUTES"])
    print("NOT ENOUGH INFO          :", labels["NOT ENOUGH INFO"])
    print()
    print("Evidence available :", evidence_available)
    print("Evidence missing:", evidence_missing)
