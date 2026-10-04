# Secure Enterprise RAG

Level: 7 — Intermediate & Advanced RAG

Skills: Python, a redaction gate before retrieve

Refuse questions that contain secret-looking tokens (password, api_key, bearer). Applied stays false.

```bash
pip install -r requirements.txt
pytest -q
```

This is a local laptop proof. It does not call a hosted model and it does not apply production changes.
