
# Formal Conjectures AI review

This is a repository for tracking AI reviews of statements in the [`formal-conjectures`](https://github.com/google-deepmind/formal-conjectures) repository. We aim to do this in a way that makes it clear what versions of what conjecture statements have been reviewed by which models, so that it is easy to see programmatically what work would provide useful additional coverage, and what the most pressing unaddressed problems with `formal-conjectures` currently are.

The current highest-priority issues are listed in [top_issues.md](top_issues.md), which CI regenerates whenever audits change.

It should be possible to contribute reviews by pointing an agent at [CONTRIBUTING.md](CONTRIBUTING.md).
You should feel free to read that file to understand the process and submit issues and pull requests to it if there is anything unclear or that could be improved.

## Prioritizing Issues

Bug-finding capabilities can vary in odd ways from model to model, with some models finding some bugs and other models finding others.
We therefore take the philosophy that if any model assigns a high severity score to a declaration, we should consider the issue to be high priority, even if other models do not report a problem. We might need to revisit this stance if we find some models are not of high enough quality to avoid false positives. That being said, we maintain a [top_issues.md](top_issues.md) via a CI hook which prioritizes reviews by the following procedure:

1. We consider all (declaration, model) pairs for which the declaration is still present in the most recent version of `formal-conjectures` and there is at least one review of the declaration by the model.
2. For all such (declaration, model) pairs, we consider the most recent review of that declaration by that model.
3. We sort such audits by severity and then by recency, and write these results to [top_issues.md](top_issues.md) with a CI hook.

Updating this file should be done using the [scripts/top_issues.py](scripts/top_issues.py) script. If a change is made to `formal-conjectures` to address an audit, then ideally, a re-review of that fixed declaration can be made with all available models (indeed, declarations that have had issue before perhaps deserve high scrutiny in general).