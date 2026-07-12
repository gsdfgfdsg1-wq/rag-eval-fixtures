#!/usr/bin/env python3
"""Evaluate RAG retrieval results against versioned golden evidence fixtures."""
import argparse
import json
from datetime import date
from pathlib import Path


def evaluate(fixtures, results, today=None):
    today = today or date.today().isoformat()
    result_map = {item["id"]: set(item.get("retrieved", [])) for item in results}
    rows = []
    for fixture in fixtures:
        gold = set(fixture.get("evidence", [])); retrieved = result_map.get(fixture["id"], set())
        hits = gold & retrieved
        rows.append({"id": fixture["id"], "recall": len(hits) / len(gold) if gold else 1, "citation_precision": len(hits) / len(retrieved) if retrieved else 0, "expired": bool(fixture.get("expires_at") and fixture["expires_at"] < today)})
    return {"fixtures": rows, "average_recall": sum(row["recall"] for row in rows) / len(rows) if rows else 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixtures"); parser.add_argument("results")
    args = parser.parse_args()
    print(json.dumps(evaluate(json.loads(Path(args.fixtures).read_text()), json.loads(Path(args.results).read_text())), indent=2))


if __name__ == "__main__":
    main()
