# Top issues

The most urgent misformalizations reported by audits, ranked as described in CONTRIBUTING.md.

1. `Erdos142.erdos_142.variants.isTheta`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/142.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/ErdosProblems/142.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5, MathArena score 83.3
   - **Audit file:** [Erdos142-erdos_142-variants-isTheta.json](audits/FormalConjectures/ErdosProblems/142/Erdos142-erdos_142-variants-isTheta.json)

   This has the same defect as erdos_142. `isTheta.answer : ℕ → ℝ` is independent of k, but the statement asserts r_k(N) ≍ answer(N) for every k. With k = 1 (r_1(N) = N) and k = 3 (r_3(N) = o(N), Roth), no single function works, so the statement is provably false. The answer should depend on k (and k ≥ 3 should be assumed).

   </details>

2. `Erdos142.erdos_142`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/142.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/ErdosProblems/142.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5, MathArena score 83.3
   - **Audit file:** [Erdos142-erdos_142.json](audits/FormalConjectures/ErdosProblems/142/Erdos142-erdos_142.json)

   The intent (Erdős #142) is an asymptotic formula for r_k(N). However, `erdos_142.answer : ℕ → ℝ` does not depend on k, while the theorem is quantified over every k. The same function would have to be asymptotic to r_k for all k simultaneously. This is impossible: by the file's own API, maxCard 1 N = N, whereas r_3(N) = o(N) by Roth's theorem. So r_1 ~ answer ~ r_3 is contradictory, and the statement is provably false for every choice of answer, so it cannot capture the problem. Fix: make the answer a function of k (answer : ℕ → ℕ → ℝ) and restrict to k ≥ 3.

   </details>

3. `Erdos319.erdos_319`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/319.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/ErdosProblems/319.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5, MathArena score 83.3
   - **Audit file:** [Erdos319-erdos_319.json](audits/FormalConjectures/ErdosProblems/319/Erdos319-erdos_319.json)

   The intent (Erdős #319) is the largest A ⊆ [N] admitting signs δ with Σ δ_n/n = 0 and no vanishing proper non-empty subsum. However, `erdos_319.answer : ℕ` is a single constant, while the theorem asserts IsGreatest {…} answer for every N. The maximum genuinely depends on N: it is 0 for N = 1 (only A = ∅ qualifies) and ≥ (1 − 1/e + o(1))N for large N (erdos_319.variants.lb). So the statement is provably false for every value of the answer. The answer should be a function of N (answer : ℕ → ℕ).

   </details>

4. `Erdos321.erdos_321`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/321.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/ErdosProblems/321.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5, MathArena score 83.3
   - **Audit file:** [Erdos321-erdos_321.json](audits/FormalConjectures/ErdosProblems/321/Erdos321-erdos_321.json)

   The intent (Erdős #321) is R(N), the largest A ⊆ [N] with all subset sums of reciprocals distinct. However, `erdos_321.answer : ℕ` is a single constant, while the theorem asserts R N = answer for every N. R(N) is unbounded (R(N) ≫ N/log N by Bleicher–Erdős) and R(1) = 1, so no constant works and the statement is provably false. The answer should be a function of N.

   </details>

5. `OeisA103425.conjecture.variants.nonconstant`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/OEIS/103425.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/OEIS/103425.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5, MathArena score 83.3
   - **Audit file:** [OeisA103425-conjecture-variants-nonconstant.json](audits/FormalConjectures/OEIS/103425/OeisA103425-conjecture-variants-nonconstant.json)

   Same issue as OeisA103425.conjecture: the OEIS A103425 question concerns weighted tribonacci sequences in the sense of A102001 (sequences determined by (a, b, c) with canonical initial terms), but the formal version allows arbitrary initial values. Requiring x to be nonconstant does not repair this: x(n) = 4(n+1) satisfies x(n+3) = x(n+2) + x(n+1) − x(n) and is trivially prime-free. The statement is true and proved, but it does not capture the intended question.

   </details>

6. `OeisA103425.conjecture.variants.nonconstant_distinct_coeffs`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/OEIS/103425.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/OEIS/103425.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5, MathArena score 83.3
   - **Audit file:** [OeisA103425-conjecture-variants-nonconstant_distinct_coeffs.json](audits/FormalConjectures/OEIS/103425/OeisA103425-conjecture-variants-nonconstant_distinct_coeffs.json)

   Same issue as OeisA103425.conjecture: with arbitrary initial values, the polynomial sequence x(n) = (n+2)² satisfies the (3, −3, 1) recurrence and is never prime, so the 'pairwise distinct coefficients, nonconstant' variant is trivial. The OEIS A103425 question (weighted tribonacci sequences as in A102001, determined by (a, b, c)) is not captured. True and proved, but not the intended question.

   </details>

7. `OeisA103425.conjecture`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/OEIS/103425.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/OEIS/103425.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5, MathArena score 83.3
   - **Audit file:** [OeisA103425-conjecture.json](audits/FormalConjectures/OEIS/103425/OeisA103425-conjecture.json)

   OEIS A103425 (J. Vos Post): 'This is a (3, 1, −3) weighted tribonacci sequence, cf. A102001 ... Is there an (a, b, c) weighted tribonacci sequence with a, b, c relatively prime which is prime-free?' In the cited A102001 a weighted tribonacci sequence is a specific sequence generated from the coefficients (1/(1 − ax − bx² − cx³), i.e. fixed canonical initial terms), and A103425 itself has fixed initial terms. The formal IsWeightedTribonacci a b c x only constrains the recurrence and leaves x's initial values arbitrary, so the question becomes trivial: x ≡ 0 or x ≡ 4 with (1, 1, −1) works, as the docstring's witness shows. That interpretation almost certainly misses the intended question (the canonical sequence determined by (a, b, c), or at least a non-degenerate one), whose answer is not settled by a constant sequence. So the 'research solved' status rests on a degenerate reading. Concrete discrepancy: the initial terms of x are unconstrained.

   </details>

8. `DiophantineTuple.hasUniqueExtension_of_forall`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/Wikipedia/DiophantineTuple.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/Wikipedia/DiophantineTuple.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5, MathArena score 83.3
   - **Audit file:** [DiophantineTuple-hasUniqueExtension_of_forall.json](audits/FormalConjectures/Wikipedia/DiophantineTuple/DiophantineTuple-hasUniqueExtension_of_forall.json)

   The strong Diophantine quintuple conjecture: every Diophantine triple {a, b, c} has at most one extension by d > max(a, b, c), namely the regular one. Because 0 is allowed in the definition, the triple {0, 1, 3} is "Diophantine" (products plus one: 1, 1, 4). It has two extensions with d > 3: d = 8 and d = 120, since d + 1 and 3d + 1 are both squares. Hence HasUniqueExtensionOfForall is false as formalized and the open conjecture is trivially disproved. Excluding 0 from the definition repairs it.

   </details>

9. `DiophantineTuple.noIntegralDiophantineFiveTuple`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/Wikipedia/DiophantineTuple.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/Wikipedia/DiophantineTuple.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5, MathArena score 83.3
   - **Audit file:** [DiophantineTuple-noIntegralDiophantineFiveTuple.json](audits/FormalConjectures/Wikipedia/DiophantineTuple/DiophantineTuple-noIntegralDiophantineFiveTuple.json)

   Intended as the He–Togbé–Ziegler theorem (no Diophantine quintuple of positive integers). However, IsDiophantineTuple does not exclude 0, even though its docstring says "each element is nonzero" and IsIntegralDiophantineTuple claims to be about positive integers. Since 0·x + 1 = 1 is a square, {0, 1, 3, 8, 120} is an IsIntegralDiophantineTuple of cardinality 5 (I verified all ten products numerically). So NoIntegralDiophantineFiveTuple is false as formalized, and this "research solved" theorem is unprovable. Fix: add x ≠ 0 (or 0 < x) to the definition.

   </details>

10. `DiophantineTuple.rational_7_tuple`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/Wikipedia/DiophantineTuple.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/Wikipedia/DiophantineTuple.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5, MathArena score 83.3
   - **Audit file:** [DiophantineTuple-rational_7_tuple.json](audits/FormalConjectures/Wikipedia/DiophantineTuple/DiophantineTuple-rational_7_tuple.json)

   "Does there exist a rational Diophantine 7-tuple?", stated as existence. With 0 not excluded from IsDiophantineTuple, Gibbs' 6-tuple {11/192, 35/192, 155/27, 512/27, 1235/48, 180873/16} together with 0 is a 7-element "rational Diophantine tuple". I verified this numerically, since 0·x + 1 = 1. So the open question is trivially answered "yes" under this formalization. The definition must require nonzero elements, as its own docstring states.

   </details>
