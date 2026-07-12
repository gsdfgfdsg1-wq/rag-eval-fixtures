# rag-eval-fixtures

A dependency-free CLI for evaluating RAG retrieval results against versioned golden evidence fixtures.

## Quick start

```bash
python evaluate.py fixtures.json results.json
```

Fixtures define question IDs, gold evidence IDs, and optional expiry dates. Results provide retrieved evidence IDs. The report calculates per-fixture recall, citation precision, expired fixtures, and average recall.

## Test

```bash
python -m unittest discover -v
```

## License

MIT.
