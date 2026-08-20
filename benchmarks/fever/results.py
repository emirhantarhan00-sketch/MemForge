from collections import Counter
from collections.abc import Mapping
from enum import Enum
import json
from datetime import datetime, timezone
from pathlib import Path
from dataclasses import asdict, is_dataclass, fields

def make_json_safe(obj, seen= None):
    if seen is None:
        seen = set()

    if obj is None or isinstance(obj, (str, int, float, bool)):
        return obj

    obj_id = id(obj)

    if obj_id in seen:
        return "<circular reference>"
    
    seen.add(obj_id)

    if isinstance(obj, dict):
        return{
            str(key): make_json_safe( value, seen)
            for key,  value in obj.items()
        }
    if isinstance(obj, (list, tuple, set)):
        return[
            make_json_safe(value, seen)
            for value in obj
        ]
    if is_dataclass(obj):
        return{
            field.name: make_json_safe(getattr(obj, field.name), seen)
            for field in fields (obj)
        }
    if hasattr(obj, "__dict__"):
        return{
            key: make_json_safe(value, seen)
            for key, value in obj.__dict__.items()
        }
    return str(obj)
       

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



def save_results (results):
    output_dir = Path("benchmark results") / "fever"
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")

    output_file = output_dir / f"fever_{timestamp}.json"
    latest_file = output_dir / "latest.json"

    with output_file.open('w', encoding="utf-8") as f:
        json.dump(
           make_json_safe(results),
           f,
           indent=2,
           ensure_ascii=False
        )

    with latest_file.open("w", encoding="utf-8") as f:
        json.dump(
           make_json_safe(results),
            f, 
            indent=2, 
            ensure_ascii=False,
        )
    print()
    print(f"Results saved to:{output_file}")
