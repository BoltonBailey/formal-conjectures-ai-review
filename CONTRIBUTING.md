
# Contributing

This file is intended to be readable by AIs in order to assist them with the process of auditing `formal-conjectures`, a repository which contains conjectures in mathematics formally stated in Lean.

## How to conduct an audit

1. Clone https://github.com/google-deepmind/formal-conjectures and note the commit hash you are reviewing (`git rev-parse HEAD`).
2. Choose a declaration to audit. Prefer declarations with no existing audit, or whose existing audits are stale or come from weaker models (see [Program for sorting audits](#program-for-sorting-audits)). Test declarations (`@[category test]`) do not need audits.
3. Read the declaration, its docstring, and every definition it depends on, including those in `FormalConjecturesForMathlib`. Read the upstream `CONTRIBUTING.md` for formal-conjectures' conventions (e.g. how `@[question]` statements are phrased).
4. Compare the statement with the source it cites (the erdosproblems.com page, OEIS entry, paper, etc.). If you cannot access the source, do not submit an audit for that declaration.
5. Record the result as described below and open a pull request. Run `python3 scripts/validate_audits.py` before submitting.

## Model list

We maintain a list of models in [models.json](models.json), scored by their "expected performance" on the overall leaderboard at [MathArena](https://matharena.ai/models). We use these scores to make determinations about which audits are most important to address first.

MathArena ranks each model at a particular effort level, so models.json has one entry per (model, effort) pair, with these fields:

* `id`: The model's API identifier (e.g. `claude-opus-5-5`). This is what goes in the `model` field of an audit.
* `effort`: The effort level of the MathArena entry (e.g. `"high"`), or `null` if MathArena does not specify one.
* `matharena`: The model's slug on MathArena, so that `https://matharena.ai/models/<slug>` is its page, or `null` if MathArena has not evaluated it.
* `score`: The MathArena expected performance, as a percentage (e.g. `83.3`), or `null` if MathArena has not evaluated it.
* `as_of`: The date the score was read from MathArena (`YYYY-MM-DD`).

If the model you are using is not in the list, add an entry for it in your PR, copying its score from MathArena. An audit is scored using the entry matching both its `model` and `effort`. If no entry matches the effort, the audit gets the lowest score listed for that model. If the model has no score at all, its audits sort last.

## JSON format for audits

The result of an audit should be a PR to this repository which adds a JSON file to the `audits/` directory. The directory structure of `audits/` should reflect that of `formal-conjectures`, with audit files for particular declarations appearing in a file that matches the directory, filename, and dash-separated fully qualified name of the declaration being audited, for example:

`audits/FormalConjectures/ErdosProblems/508/Erdos508-HadwigerNelsonProblem.json`

audits the declaration `Erdos508.HadwigerNelsonProblem` in `FormalConjectures/ErdosProblems/508.lean`.

The JSON file should contain a list of audit entries. If the file already exists, append a new entry to the list rather than replacing existing entries. Each entry is an object with the following fields:

* `hash`: The commit hash of the version of `formal-conjectures` reviewed (full 40-character hex).
* `model`: The model that completed the review, which must appear in [models.json](models.json).
* `effort`: The reasoning effort level the model was run at (e.g. `"low"`, `"high"`, `"max"`), or `null` if unknown or not applicable.
* `severity`: The result of the audit, as a severity rank 1-5 with the following meanings:
    1. The problem is correctly formulated.
    2. The problem is mostly correctly formulated, perhaps with unclear documentation.
    3. The problem has some edge cases or discrepancies which make it distinct from all usual ways of formulating the problem, but solving the problem is still ultimately equivalent to the desired problem.
    4. The problem is essentially misformalized, in that it is unclear whether the result is a correct formulation.
    5. The problem is misformulated, in a way that makes the provability of the stated problem different from the intended mathematical statement.
* `explanation`: Explanation from the model of the reported result. Cite the source you compared against, and for severity 3 and above, say concretely what the discrepancy is.

For example

```json
[
    {
        "hash": "e750f777b32aeae464c01809e0d223dd62e99fab",
        "model": "claude-opus-5-5",
        "effort": "high",
        "severity": 1,
        "explanation": "Matches the problem as stated on erdosproblems.com/508: ..."
    }
]
```

## Program for sorting audits

We sort audits that report misformalizations by urgency, using these criteria, in order.

1. Does the audit report a misformalization (severity 4 or 5)?
2. How strong was the model that conducted the audit, according to its score in [models.json](models.json)? Audits from stronger models come first.
3. How recent is the `formal-conjectures` commit the audit was conducted on? Audits of more recent commits come first, since the reported problem is less likely to have been addressed already.
4. Higher severity comes first.

[scripts/sort_audits.py](scripts/sort_audits.py) prints audits in this order. Criterion 3 needs a clone of formal-conjectures with full history, passed as `--upstream`, so that commit dates can be looked up. A blobless clone is enough and does not require building anything:

```sh
git clone --filter=blob:none https://github.com/google-deepmind/formal-conjectures
python3 scripts/sort_audits.py --upstream formal-conjectures
```

[scripts/top_issues.py](scripts/top_issues.py) takes the same `--upstream` option and writes the ten most urgent issues to [top_issues.md](top_issues.md), one per declaration, with each audit's details collapsed. CI regenerates and commits this file on every push to `main` that changes audits, models.json or the scripts, so do not edit it by hand or include it in your PR.

## CI

CI on this repo enforces the consistency of the JSON by running [scripts/validate_audits.py](scripts/validate_audits.py), which checks file paths, field names and types, severity range, that every model appears in [models.json](models.json), and the format of models.json itself.
