# Top issues

The most urgent misformalizations reported by audits, ranked as described in CONTRIBUTING.md.

1. `Erdos918.erdos_918.variants.eq_aleph_0.parts.i`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/918.lean](https://github.com/google-deepmind/formal-conjectures/blob/e750f777b32aeae464c01809e0d223dd62e99fab/FormalConjectures/ErdosProblems/918.lean)
   - **Commit:** [`e750f777b32a`](https://github.com/google-deepmind/formal-conjectures/commit/e750f777b32aeae464c01809e0d223dd62e99fab) (2026-10-15)
   - **Model:** claude-opus-5-5, MathArena score 83.3
   - **Audit file:** [Erdos918-erdos_918-variants-eq_aleph_0-parts-i.json](audits/FormalConjectures/ErdosProblems/918/Erdos918-erdos_918-variants-eq_aleph_0-parts-i.json)

   This variant asserts that no graph on aleph_2 vertices with chromatic number aleph_2 has every INDUCED subgraph on aleph_1 vertices of chromatic number exactly aleph_0, and is tagged `@[category textbook]`, i.e. claimed to be a known result. The only justification in the sources (erdosproblems.com/918, crediting louisd) is for (not necessarily induced) subgraphs: an edgeless subgraph on aleph_1 vertices has chromatic number 1, so the '= aleph_0' version is trivially impossible. The file's own formalisation note concedes this argument does not carry over to induced subgraphs. For induced subgraphs the statement needs an aleph_1-set W whose induced chromatic number is finite or at least aleph_1. Under CH this follows from Erdős–Rado (aleph_2 -> (aleph_1)^2 gives an independent set or clique of size aleph_1), but without CH, aleph_2 -/-> (aleph_1)^2 is consistent (a Sierpiński-type colouring when 2^aleph_0 >= aleph_2), and then the statement appears entangled with the open main question erdos_918.parts.i. I found no source establishing the statement in ZFC, so the `textbook` label (and plausibly the provability of the statement in ZFC) is unsupported. Suggested fix: retag as open, or restrict the variant to the all-subgraphs form already stated as erdos_918.variants.eq_aleph_0_all_subgraphs.parts.i. The same concern applies to erdos_918.variants.eq_aleph_0.parts.ii.

   </details>
