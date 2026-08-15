def fever_to_claim(record:dict) ->dict:
    return{
        "id": record["id"],
        "claim": record["claim"],
        "evidence": record.get("evidence", []),
        "ground_truth": record["label"],
        "verifiable": record.get("verifiable"),
    }