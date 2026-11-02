# Top issues

The most urgent misformalizations reported by audits, ranked as described in CONTRIBUTING.md.

1. `Erdos1017.erdos_1017.lower_bound`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/1017.lean](https://github.com/google-deepmind/formal-conjectures/blob/d995ef5d306637c0a2e489c7e579647168d7df2f/FormalConjectures/ErdosProblems/1017.lean)
   - **Commit:** [`d995ef5d3066`](https://github.com/google-deepmind/formal-conjectures/commit/d995ef5d306637c0a2e489c7e579647168d7df2f) (2026-11-01)
   - **Model:** claude-opus-5-5, MathArena score 83.3
   - **Audit file:** [Erdos1017-erdos_1017-lower_bound.json](audits/FormalConjectures/ErdosProblems/1017/Erdos1017-erdos_1017-lower_bound.json)

   The source at erdosproblems.com/1017 says 'Estimate f(n,k) for k>n²/4', a vague request (the page says Erdős asks vaguely). Discrepancy: the Lean statement only asks for some function answer with answer n k≤f n k, so answer≡0 proves it with no content. Upstream STATEMENTS.md asks that a value statement constrain the unknown. Whether this is a correct formulation of the problem is therefore unclear, and proving it says nothing about the estimate.

   </details>

2. `Erdos1017.erdos_1017.upper_bound`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/1017.lean](https://github.com/google-deepmind/formal-conjectures/blob/d995ef5d306637c0a2e489c7e579647168d7df2f/FormalConjectures/ErdosProblems/1017.lean)
   - **Commit:** [`d995ef5d3066`](https://github.com/google-deepmind/formal-conjectures/commit/d995ef5d306637c0a2e489c7e579647168d7df2f) (2026-11-01)
   - **Model:** claude-opus-5-5, MathArena score 83.3
   - **Audit file:** [Erdos1017-erdos_1017-upper_bound.json](audits/FormalConjectures/ErdosProblems/1017/Erdos1017-erdos_1017-upper_bound.json)

   The source at erdosproblems.com/1017 says 'Estimate f(n,k) for k>n²/4'. Discrepancy: the Lean statement only needs f n k≤answer n k, so taking answer n k:=f n k, or n²/4-type bounds from the Erdős-Goodman-Pósa theorem quoted on the page, proves it. It therefore does not capture any sharpening, which the page says is what Erdős was asking about.

   </details>

3. `Erdos328.erdos_328`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/328.lean](https://github.com/google-deepmind/formal-conjectures/blob/d995ef5d306637c0a2e489c7e579647168d7df2f/FormalConjectures/ErdosProblems/328.lean)
   - **Commit:** [`d995ef5d3066`](https://github.com/google-deepmind/formal-conjectures/commit/d995ef5d306637c0a2e489c7e579647168d7df2f) (2026-11-01)
   - **Model:** claude-opus-5-5, MathArena score 83.3
   - **Audit file:** [Erdos328-erdos_328.json](audits/FormalConjectures/ErdosProblems/328/Erdos328-erdos_328.json)

   The statement ¬ ∀ C > 0, ∃ t, … is trivially provable with C = 1. Take A = {1}: sumRep A n ≤ 1 for all n, since only n = 2 is represented, once. Any partition must put 1 into some piece P i, and then sumRep (P i) 2 = 1, which is not < 1. With t = 0 the union is empty and cannot equal A. So the formal statement does not capture the content of Nešetřil–Rödl, who show the answer is no for every C, nor Erdős's C = 3, 4 results. Small C are degenerate under the ordered-pair convolution. Simply switching to ∀ C > 0, ¬ ∃ t, … with the ordered sumRep does not fix it, because that is false at C = 3. Ordered count ≤ 3 means each b ∈ A is the middle of at most one progression a < b < c in A, so colouring greedily with b opposite a gives t = 2. A faithful version should count unordered pairs a ≤ b, as in Nešetřil–Rödl Theorem 2, and state ∀ C > 0, ¬ ∃ t, …, ideally even with t depending on A. See issue #6540 and PR #7704.

   </details>

4. `Erdos918.erdos_918.variants.eq_aleph_0.parts.i`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/918.lean](https://github.com/google-deepmind/formal-conjectures/blob/e750f777b32aeae464c01809e0d223dd62e99fab/FormalConjectures/ErdosProblems/918.lean)
   - **Commit:** [`e750f777b32a`](https://github.com/google-deepmind/formal-conjectures/commit/e750f777b32aeae464c01809e0d223dd62e99fab) (2026-10-15)
   - **Model:** claude-opus-5-5, MathArena score 83.3
   - **Audit file:** [Erdos918-erdos_918-variants-eq_aleph_0-parts-i.json](audits/FormalConjectures/ErdosProblems/918/Erdos918-erdos_918-variants-eq_aleph_0-parts-i.json)

   This variant asserts that no graph on aleph_2 vertices with chromatic number aleph_2 has every INDUCED subgraph on aleph_1 vertices of chromatic number exactly aleph_0, and is tagged `@[category textbook]`, i.e. claimed to be a known result. The only justification in the sources (erdosproblems.com/918, crediting louisd) is for (not necessarily induced) subgraphs: an edgeless subgraph on aleph_1 vertices has chromatic number 1, so the '= aleph_0' version is trivially impossible. The file's own formalisation note concedes this argument does not carry over to induced subgraphs. For induced subgraphs the statement needs an aleph_1-set W whose induced chromatic number is finite or at least aleph_1. Under CH this follows from Erdős–Rado (aleph_2 -> (aleph_1)^2 gives an independent set or clique of size aleph_1), but without CH, aleph_2 -/-> (aleph_1)^2 is consistent (a Sierpiński-type colouring when 2^aleph_0 >= aleph_2), and then the statement appears entangled with the open main question erdos_918.parts.i. I found no source establishing the statement in ZFC, so the `textbook` label (and plausibly the provability of the statement in ZFC) is unsupported. Suggested fix: retag as open, or restrict the variant to the all-subgraphs form already stated as erdos_918.variants.eq_aleph_0_all_subgraphs.parts.i. The same concern applies to erdos_918.variants.eq_aleph_0.parts.ii.

   </details>
