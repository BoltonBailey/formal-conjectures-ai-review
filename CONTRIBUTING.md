
# Contributing

This file is intended to be readable by AIs in order to assist them with the process of auditing `formal-conjectures`, a repository which contains conjectures in mathematics formally stated in Lean.

## Model list

We maintain a list of models, ordered by strength of performance of the TODO benchmark at TODO. We use this ordering to make determinations about which audits are most important to address first.

## JSON format for audits

The result of an audit should be a PR to this repository which adds a JSON file to the `audits/` directory. The directory structure of `audits/` should reflect that of `formal-conjectures`, with audit files for particular declarations appearing in a file that matches the directory, filename, and dash-separated fully qualified name of the declaration baing audited, for example:

`audits/FormalConjectures/ErdosProblems/508/Erdos508-HadwigerNelsonProblem.json`

The JSON file should contain a list of audit entries with the following fields:

* The commit hash of the version of `formal-conjectures` reviewed
* The model completed the reviewing, coming from some predefined list
    * I guess we should track effort level too?
* The result of the audit, as a severity rank 1-5 with the following meanings:
    1. The problem is correctly formulated.
    2. The problem is mostly correctly formulated, perhaps with unclear documentation.
    3. The problem has some edge cases or discrepancies which make it distinct for all usual ways of formulating the problem, but solving the problem is still ultimately equivalent to the desired problem.
    4. The problem is essentially misformalized, in that it is unclear whether the result is a correct formulation.
    5. The problem is misformulated, in a way that makes the provability of the stated problem different from the intended mathematical statement.
* Explanation from the model of the reported result.

For example

```json
[
    {
        "hash": "e750f777b32aeae464c01809e0d223dd62e99fab"
        TODO
    }
]
```

## Program for sorting audits

We sort audits that report misformalizations by urgency, using these criteria, in order.

1. Does the audit report a misformalization?
2. Has the dependency tree of the file in which the audited file occurs changed since the audit was conducted?
3. How strong was the model that 

## TODO CI

CI on this repo should enforce the consistency of the JSON