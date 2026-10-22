"""Shared helpers for reading models.json and the audit files."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AUDITS = ROOT / "audits"
MODELS = ROOT / "models.json"
MODEL_FIELDS = {"id", "effort", "matharena", "score", "as_of"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def load_models():
    return json.loads(MODELS.read_text(encoding="utf-8"))


def validate_models(models):
    """Return a list of error messages for the contents of models.json."""
    if not isinstance(models, list):
        return ["models.json must be a list of model entries"]
    errors = []
    seen = set()
    for i, m in enumerate(models):
        if not isinstance(m, dict):
            errors.append(f"models.json entry {i}: not an object")
            continue
        if set(m) != MODEL_FIELDS:
            errors.append(f"models.json entry {i}: fields must be exactly {sorted(MODEL_FIELDS)}")
            continue
        if not (isinstance(m["id"], str) and m["id"]):
            errors.append(f"models.json entry {i}: `id` must be a non-empty string")
        if not (m["effort"] is None or isinstance(m["effort"], str)):
            errors.append(f"models.json entry {i}: `effort` must be a string or null")
        if not (m["matharena"] is None or isinstance(m["matharena"], str)):
            errors.append(f"models.json entry {i}: `matharena` must be a string or null")
        score = m["score"]
        if not (score is None or (type(score) in (int, float) and 0 <= score <= 100)):
            errors.append(f"models.json entry {i}: `score` must be a percentage or null")
        if not (isinstance(m["as_of"], str) and DATE_RE.match(m["as_of"])):
            errors.append(f"models.json entry {i}: `as_of` must be a YYYY-MM-DD date")
        key = (m["id"], m["effort"])
        if key in seen:
            errors.append(f"models.json entry {i}: duplicate (id, effort) pair {key}")
        seen.add(key)
    return errors


def model_score(models, model, effort):
    """The MathArena score for an audit by `model` at `effort`.

    Uses the entry matching both, else the lowest score listed for `model`, else None.
    """
    entries = [m for m in models if m["id"] == model and m["score"] is not None]
    for m in entries:
        if m["effort"] == effort:
            return m["score"]
    return min((m["score"] for m in entries), default=None)


def audit_files():
    return sorted(p for p in AUDITS.rglob("*") if p.is_file()) if AUDITS.is_dir() else []


def lean_file_for(audit_path):
    """The formal-conjectures Lean file (relative path) that an audit file refers to."""
    rel = audit_path.relative_to(AUDITS)
    return Path(*rel.parts[:-1]).with_suffix(".lean")
