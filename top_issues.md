# Top issues

The issues that audits currently report, ranked as described in the [Prioritizing Issues](README.md#prioritizing-issues) section of the README: each entry is a model's most recent audit of a declaration that is still present in `formal-conjectures`, with severity at least 3, sorted by severity and then by how recent the audited commit is.

1. `Erdos503.erdos_503`: severity 5, misformulated (provability differs)

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/503.lean](https://github.com/google-deepmind/formal-conjectures/blob/a425ca3eb797fe927cb88c950565fdcbbbbada70/FormalConjectures/ErdosProblems/503.lean)
   - **Commit:** [`a425ca3eb797`](https://github.com/google-deepmind/formal-conjectures/commit/a425ca3eb797fe927cb88c950565fdcbbbbada70) (2026-11-12)
   - **Model:** claude-fable-5-2
   - **Audit file:** [Erdos503-erdos_503.json](audits/FormalConjectures/ErdosProblems/503/Erdos503-erdos_503.json)

   Compared against erdosproblems.com/503: 'What is the size of the largest A ⊆ R^d such that every three points from A determine an isosceles triangle?' — a quantity that depends on the dimension d (6 for d = 2, 8 for d = 3, between C(d+1,2)+1 and C(d+2,2) in general). In the Lean file the answer is declared as a single natural number, 'def erdos_503.answer : ℕ := sorry', while the theorem is 'theorem erdos_503 (n : ℕ) : IsGreatest {A.ncard | A : Set (ℝ^n), A.IsIsosceles} erdos_503.answer', universally quantified over the dimension n. No value of the constant can satisfy this for all n: the file's own solved variants erdos_503.variants.R2 and erdos_503.variants.R3 state that the greatest element is 6 for n = 2 and 8 for n = 3 (and for n = 0 it is 1), and IsGreatest determines its value uniquely. So the statement as written is false for every choice of erdos_503.answer and cannot express the intended problem. The intended form is an answer depending on the dimension, e.g. 'def erdos_503.answer : ℕ → ℕ := sorry' with conclusion 'IsGreatest {...} (erdos_503.answer n)'. The rest of the encoding (Set.IsIsosceles = nonempty and every triple of distinct points has two equal distances; ncard; ℝ^n as Euclidean space) is fine.

   </details>

2. `Erdos506.erdos_506`: severity 5, misformulated (provability differs)

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/506.lean](https://github.com/google-deepmind/formal-conjectures/blob/da703a5f239f734a47ede2f4e99b9ccc9e644cb5/FormalConjectures/ErdosProblems/506.lean)
   - **Commit:** [`da703a5f239f`](https://github.com/google-deepmind/formal-conjectures/commit/da703a5f239f734a47ede2f4e99b9ccc9e644cb5) (2026-11-11)
   - **Model:** claude-fable-5-2
   - **Audit file:** [Erdos506-erdos_506.json](audits/FormalConjectures/ErdosProblems/506/Erdos506-erdos_506.json)

   Compared against erdosproblems.com/506: 'What is the minimum number of circles determined by any n points in ℝ², not all on a circle?' — a value question whose answer is a function of n (for n > 393 it is C(n−1,2) + 1 − ⌊(n−1)/2⌋ by Elliott with the Purdy–Smith correction). Concrete defect: the Lean unknown is declared as `def erdos_506.answer : ℕ := sorry`, a single natural number independent of n, while the theorem asserts, for every n ≥ 4, IsLeast {numCircles P : |P| = n, P not collinear, not cospherical} erdos_506.answer. Since the minimum changes with n — e.g. the file's own large_n variant gives 76833 for n = 394 and 77225 for n = 395 — no single natural number can be the least element for all n, so the statement is false for every choice of answer and can never be 'solved' as intended. The answer should have type ℕ → ℕ (as erdos_506.variants.large_n.answer does). The same defect affects erdos_506.variants.small_n (constant answer for all 4 ≤ n ≤ 393). The rest (numCircles, non-degeneracy assumptions, n ≥ 4) is reasonable.

   </details>

3. `Erdos525.erdos_525.parts.ii`: severity 5, misformulated (provability differs)

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/525.lean](https://github.com/google-deepmind/formal-conjectures/blob/2f91d251c07fbbaf9435166d47c11e884a08a6cf/FormalConjectures/ErdosProblems/525.lean)
   - **Commit:** [`2f91d251c07f`](https://github.com/google-deepmind/formal-conjectures/commit/2f91d251c07fbbaf9435166d47c11e884a08a6cf) (2026-11-09)
   - **Model:** claude-fable-5-2
   - **Audit file:** [Erdos525-erdos_525-parts-ii.json](audits/FormalConjectures/ErdosProblems/525/Erdos525-erdos_525-parts-ii.json)

   Compared against erdosproblems.com/525 and the cited paper, Cook–Nguyen, 'Universality of the minimum modulus for random trigonometric polynomials' (Discrete Analysis 2021:20, arXiv:2101.07203v3). The site only says lim P(m(f) > ε n^{-1/2}) = e^{-ελ} 'where λ is an explicit constant'; the Lean statement fixes λ = √(π/12), and this value appears to be wrong by a factor of 2. In the paper (eqs. (1.4)–(1.6), Theorem 1.1 and Corollary 1.5, which covers Rademacher signs) the normalised polynomial is P_n(x) = (2n+1)^{-1/2} Σ_{j=-n}^{n} ξ_j e(jx), m_n = min|P_n|, and lim P(m_n > τ/n) = e^{-λτ} with λ = 2√(π/3). Up to a unimodular factor P_n is (2n+1)^{-1/2} F_{2n}, so for the degree N = 2n polynomial f = F_N of the Lean statement, m_n > τ/n means m(f) > τ√(2n+1)/n ≈ 2τ/√N. Putting ε = 2τ gives lim P(m(f) > ε/√N) = e^{-2√(π/3)·ε/2} = e^{-√(π/3) ε}, i.e. λ = √(π/3) ≈ 1.023 in the site's normalisation, not √(π/12) ≈ 0.512. (A first-moment count of near-zeros agrees: the expected number of passes of the curve within δ of 0 is δ√N·√(π/3); √(π/12) arises only as an intermediate quantity, E|P_n'|/n.) Since the limit e^{-√(π/12) ε} differs from the true limit e^{-√(π/3) ε} for every ε > 0, the Lean statement as written is false. The rest of the formalisation (uniform ±1 coefficients on Fin (n+1), m as the infimum of |f| over the unit circle, `prob` as a normalised count) is fine; I did not find the constant √(π/12) in the paper for this normalisation, and the `formal_proof` link is the same line as for part (i), so it does not appear to certify this statement.

   </details>

4. `Erdos552.erdos_552.parts.i`: severity 5, misformulated (provability differs)

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/552.lean](https://github.com/google-deepmind/formal-conjectures/blob/2f91d251c07fbbaf9435166d47c11e884a08a6cf/FormalConjectures/ErdosProblems/552.lean)
   - **Commit:** [`2f91d251c07f`](https://github.com/google-deepmind/formal-conjectures/commit/2f91d251c07fbbaf9435166d47c11e884a08a6cf) (2026-11-09)
   - **Model:** claude-fable-5-2
   - **Audit file:** [Erdos552-erdos_552-parts-i.json](audits/FormalConjectures/ErdosProblems/552/Erdos552-erdos_552-parts-i.json)

   Compared against erdosproblems.com/552 ("Determine the Ramsey number R(C_4,S_n), where S_n=K_{1,n}"). The intended object is a function of n, but the unknown is declared as a single number `erdos_552.parts.i.answer : ℕ` that does not take n as a parameter, and the statement is `∀ n, graphRamsey C_4 K_{1,n} = erdos_552.parts.i.answer`. This asserts that R(C_4,S_n) is the same for every n, which is false: the site records n+√n−6n^{11/40} ≤ R(C_4,S_n), so the values are unbounded (and the file's own docstring for `succ_le_add_two` notes R(C_4,S_0)=1 ≠ 4=R(C_4,S_1)). So the statement is false for every possible value of the answer, and no determination of R(C_4,S_n) could prove it. The upstream CONTRIBUTING.md says the answer definition should take the theorem's parameters when the unknown depends on them; the fix is `answer : ℕ → ℕ` applied to n. The graphs themselves (cycleGraph 4, completeBipartiteGraph (Fin 1) (Fin n), graphRamsey as least N such that every graph on Fin N contains C_4 or has K_{1,n} in its complement) are a correct rendering.

   </details>

5. `Arxiv.«2406.10319».pittel_hyperbola_threshold`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/Arxiv/2406.10319/StableMatchingHyperbola.lean](https://github.com/google-deepmind/formal-conjectures/blob/a919f7f47b836b766f378c2b1360b28168bbdd9d/FormalConjectures/Arxiv/2406.10319/StableMatchingHyperbola.lean)
   - **Commit:** [`a919f7f47b83`](https://github.com/google-deepmind/formal-conjectures/commit/a919f7f47b836b766f378c2b1360b28168bbdd9d) (2026-11-13)
   - **Model:** claude-fable-5-2
   - **Audit file:** [Arxiv-«2406-10319»-pittel_hyperbola_threshold.json](audits/FormalConjectures/Arxiv/2406.10319/StableMatchingHyperbola/Arxiv-«2406-10319»-pittel_hyperbola_threshold.json)

   Compared against B. Pittel, 'On Constrained Matchings, Stable Under Random Preferences' (arXiv:2406.10319, p. 26, Notes (2)). The source conjecture is a single informal sentence: 'We conjecture existence of p*(n) ∈ [9/4·log²n/n, 1], a critical threshold for appearance of a hyperbolic curve, as an asymptotic approximation of {(Q(M), R(M))}_M.' The underlying model is formalized faithfully: uniform independent preferences, each pair admissible independently with probability p (marketLaw), Gusfield–Irving stability of partial matchings (IsPartialStable), and Q, R as total ranks among admissible partners (totalWifeRank/totalHusbandRank), all as in the paper. However, the paper gives no precise meaning to 'critical threshold' or 'appearance of a hyperbolic curve', and the Lean statement supplies one through several choices that are not in the source: (a) the scaling of both ranks by √(p n³) (natural, since Theorem 1.6 gives Q ≈ R ≈ (pn³)^{1/2} below log²n/n and QR ≈ n³ at p = 1, but not stated by Pittel for intermediate p); (b) 'hyperbola appears' is defined as: every stable M has |qr − 1| ≤ ε and the fixed arc {(t, 1/t) : t ∈ [2/3, 3/2]} is ε-covered; the arc endpoints are arbitrary, and the threshold for covering this particular arc need not be the threshold at which a nondegenerate curve first appears (by Theorem 1.7, Q⁻ ≥ (1−ε) n log n for c > 9/4, so t = 2/3 can only be reached when c is about 9/4 or more, which makes the choice of arc effectively decide the location of p*); (c) the threshold is required to be sharp in a strong sense, with a relative window δ·min(p*, 1 − p*) and uniformity over all p outside the window, whereas the source's 'critical threshold' could also be coarse; (d) p* is restricted to the open interval (0,1) with a strict eventual lower bound, while the source allows the closed interval. Each choice is reasonable and the docstring documents them, but the resulting statement is one specific strengthening/interpretation among many, and its truth could differ from what Pittel intends (e.g. if the transition is not sharp in this relative sense, or if a hyperbolic arc of smaller extent appears earlier). So it is unclear that this is a correct formulation of the conjecture; the source is arguably too vague to formalize canonically.

   </details>

6. `DiophantineTuple.hasUniqueExtension_of_forall`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/Wikipedia/DiophantineTuple.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/Wikipedia/DiophantineTuple.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5
   - **Audit file:** [DiophantineTuple-hasUniqueExtension_of_forall.json](audits/FormalConjectures/Wikipedia/DiophantineTuple/DiophantineTuple-hasUniqueExtension_of_forall.json)

   The strong Diophantine quintuple conjecture: every Diophantine triple {a, b, c} has at most one extension by d > max(a, b, c), namely the regular one. Because 0 is allowed in the definition, the triple {0, 1, 3} is "Diophantine" (products plus one: 1, 1, 4). It has two extensions with d > 3: d = 8 and d = 120, since d + 1 and 3d + 1 are both squares. Hence HasUniqueExtensionOfForall is false as formalized and the open conjecture is trivially disproved. Excluding 0 from the definition repairs it.

   </details>

7. `DiophantineTuple.noIntegralDiophantineFiveTuple`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/Wikipedia/DiophantineTuple.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/Wikipedia/DiophantineTuple.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5
   - **Audit file:** [DiophantineTuple-noIntegralDiophantineFiveTuple.json](audits/FormalConjectures/Wikipedia/DiophantineTuple/DiophantineTuple-noIntegralDiophantineFiveTuple.json)

   Intended as the He–Togbé–Ziegler theorem (no Diophantine quintuple of positive integers). However, IsDiophantineTuple does not exclude 0, even though its docstring says "each element is nonzero" and IsIntegralDiophantineTuple claims to be about positive integers. Since 0·x + 1 = 1 is a square, {0, 1, 3, 8, 120} is an IsIntegralDiophantineTuple of cardinality 5 (I verified all ten products numerically). So NoIntegralDiophantineFiveTuple is false as formalized, and this "research solved" theorem is unprovable. Fix: add x ≠ 0 (or 0 < x) to the definition.

   </details>

8. `DiophantineTuple.rational_7_tuple`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/Wikipedia/DiophantineTuple.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/Wikipedia/DiophantineTuple.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5
   - **Audit file:** [DiophantineTuple-rational_7_tuple.json](audits/FormalConjectures/Wikipedia/DiophantineTuple/DiophantineTuple-rational_7_tuple.json)

   "Does there exist a rational Diophantine 7-tuple?", stated as existence. With 0 not excluded from IsDiophantineTuple, Gibbs' 6-tuple {11/192, 35/192, 155/27, 512/27, 1235/48, 180873/16} together with 0 is a 7-element "rational Diophantine tuple". I verified this numerically, since 0·x + 1 = 1. So the open question is trivially answered "yes" under this formalization. The definition must require nonzero elements, as its own docstring states.

   </details>

9. `Erdos142.erdos_142`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/142.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/ErdosProblems/142.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Erdos142-erdos_142.json](audits/FormalConjectures/ErdosProblems/142/Erdos142-erdos_142.json)

   The intent (Erdős #142) is an asymptotic formula for r_k(N). However, `erdos_142.answer : ℕ → ℝ` does not depend on k, while the theorem is quantified over every k. The same function would have to be asymptotic to r_k for all k simultaneously. This is impossible: by the file's own API, maxCard 1 N = N, whereas r_3(N) = o(N) by Roth's theorem. So r_1 ~ answer ~ r_3 is contradictory, and the statement is provably false for every choice of answer, so it cannot capture the problem. Fix: make the answer a function of k (answer : ℕ → ℕ → ℝ) and restrict to k ≥ 3.

   </details>

10. `Erdos142.erdos_142.variants.isTheta`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/142.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/ErdosProblems/142.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Erdos142-erdos_142-variants-isTheta.json](audits/FormalConjectures/ErdosProblems/142/Erdos142-erdos_142-variants-isTheta.json)

   This has the same defect as erdos_142. `isTheta.answer : ℕ → ℝ` is independent of k, but the statement asserts r_k(N) ≍ answer(N) for every k. With k = 1 (r_1(N) = N) and k = 3 (r_3(N) = o(N), Roth), no single function works, so the statement is provably false. The answer should depend on k (and k ≥ 3 should be assumed).

   </details>

11. `Erdos319.erdos_319`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/319.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/ErdosProblems/319.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Erdos319-erdos_319.json](audits/FormalConjectures/ErdosProblems/319/Erdos319-erdos_319.json)

   The intent (Erdős #319) is the largest A ⊆ [N] admitting signs δ with Σ δ_n/n = 0 and no vanishing proper non-empty subsum. However, `erdos_319.answer : ℕ` is a single constant, while the theorem asserts IsGreatest {…} answer for every N. The maximum genuinely depends on N: it is 0 for N = 1 (only A = ∅ qualifies) and ≥ (1 − 1/e + o(1))N for large N (erdos_319.variants.lb). So the statement is provably false for every value of the answer. The answer should be a function of N (answer : ℕ → ℕ).

   </details>

12. `Erdos321.erdos_321`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/321.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/ErdosProblems/321.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Erdos321-erdos_321.json](audits/FormalConjectures/ErdosProblems/321/Erdos321-erdos_321.json)

   The intent (Erdős #321) is R(N), the largest A ⊆ [N] with all subset sums of reciprocals distinct. However, `erdos_321.answer : ℕ` is a single constant, while the theorem asserts R N = answer for every N. R(N) is unbounded (R(N) ≫ N/log N by Bleicher–Erdős) and R(1) = 1, so no constant works and the statement is provably false. The answer should be a function of N.

   </details>

13. `OeisA103425.conjecture`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/OEIS/103425.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/OEIS/103425.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5
   - **Audit file:** [OeisA103425-conjecture.json](audits/FormalConjectures/OEIS/103425/OeisA103425-conjecture.json)

   OEIS A103425 (J. Vos Post): 'This is a (3, 1, −3) weighted tribonacci sequence, cf. A102001 ... Is there an (a, b, c) weighted tribonacci sequence with a, b, c relatively prime which is prime-free?' In the cited A102001 a weighted tribonacci sequence is a specific sequence generated from the coefficients (1/(1 − ax − bx² − cx³), i.e. fixed canonical initial terms), and A103425 itself has fixed initial terms. The formal IsWeightedTribonacci a b c x only constrains the recurrence and leaves x's initial values arbitrary, so the question becomes trivial: x ≡ 0 or x ≡ 4 with (1, 1, −1) works, as the docstring's witness shows. That interpretation almost certainly misses the intended question (the canonical sequence determined by (a, b, c), or at least a non-degenerate one), whose answer is not settled by a constant sequence. So the 'research solved' status rests on a degenerate reading. Concrete discrepancy: the initial terms of x are unconstrained.

   </details>

14. `OeisA103425.conjecture.variants.nonconstant`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/OEIS/103425.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/OEIS/103425.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5
   - **Audit file:** [OeisA103425-conjecture-variants-nonconstant.json](audits/FormalConjectures/OEIS/103425/OeisA103425-conjecture-variants-nonconstant.json)

   Same issue as OeisA103425.conjecture: the OEIS A103425 question concerns weighted tribonacci sequences in the sense of A102001 (sequences determined by (a, b, c) with canonical initial terms), but the formal version allows arbitrary initial values. Requiring x to be nonconstant does not repair this: x(n) = 4(n+1) satisfies x(n+3) = x(n+2) + x(n+1) − x(n) and is trivially prime-free. The statement is true and proved, but it does not capture the intended question.

   </details>

15. `OeisA103425.conjecture.variants.nonconstant_distinct_coeffs`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/OEIS/103425.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/OEIS/103425.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5
   - **Audit file:** [OeisA103425-conjecture-variants-nonconstant_distinct_coeffs.json](audits/FormalConjectures/OEIS/103425/OeisA103425-conjecture-variants-nonconstant_distinct_coeffs.json)

   Same issue as OeisA103425.conjecture: with arbitrary initial values, the polynomial sequence x(n) = (n+2)² satisfies the (3, −3, 1) recurrence and is never prime, so the 'pairwise distinct coefficients, nonconstant' variant is trivial. The OEIS A103425 question (weighted tribonacci sequences as in A102001, determined by (a, b, c)) is not captured. True and proved, but not the intended question.

   </details>

16. `Erdos1017.erdos_1017.lower_bound`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/1017.lean](https://github.com/google-deepmind/formal-conjectures/blob/d995ef5d306637c0a2e489c7e579647168d7df2f/FormalConjectures/ErdosProblems/1017.lean)
   - **Commit:** [`d995ef5d3066`](https://github.com/google-deepmind/formal-conjectures/commit/d995ef5d306637c0a2e489c7e579647168d7df2f) (2026-11-01)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Erdos1017-erdos_1017-lower_bound.json](audits/FormalConjectures/ErdosProblems/1017/Erdos1017-erdos_1017-lower_bound.json)

   The source at erdosproblems.com/1017 says 'Estimate f(n,k) for k>n²/4', a vague request (the page says Erdős asks vaguely). Discrepancy: the Lean statement only asks for some function answer with answer n k≤f n k, so answer≡0 proves it with no content. Upstream STATEMENTS.md asks that a value statement constrain the unknown. Whether this is a correct formulation of the problem is therefore unclear, and proving it says nothing about the estimate.

   </details>

17. `Erdos1017.erdos_1017.upper_bound`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/1017.lean](https://github.com/google-deepmind/formal-conjectures/blob/d995ef5d306637c0a2e489c7e579647168d7df2f/FormalConjectures/ErdosProblems/1017.lean)
   - **Commit:** [`d995ef5d3066`](https://github.com/google-deepmind/formal-conjectures/commit/d995ef5d306637c0a2e489c7e579647168d7df2f) (2026-11-01)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Erdos1017-erdos_1017-upper_bound.json](audits/FormalConjectures/ErdosProblems/1017/Erdos1017-erdos_1017-upper_bound.json)

   The source at erdosproblems.com/1017 says 'Estimate f(n,k) for k>n²/4'. Discrepancy: the Lean statement only needs f n k≤answer n k, so taking answer n k:=f n k, or n²/4-type bounds from the Erdős-Goodman-Pósa theorem quoted on the page, proves it. It therefore does not capture any sharpening, which the page says is what Erdős was asking about.

   </details>

18. `Erdos328.erdos_328`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/328.lean](https://github.com/google-deepmind/formal-conjectures/blob/d995ef5d306637c0a2e489c7e579647168d7df2f/FormalConjectures/ErdosProblems/328.lean)
   - **Commit:** [`d995ef5d3066`](https://github.com/google-deepmind/formal-conjectures/commit/d995ef5d306637c0a2e489c7e579647168d7df2f) (2026-11-01)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Erdos328-erdos_328.json](audits/FormalConjectures/ErdosProblems/328/Erdos328-erdos_328.json)

   The statement ¬ ∀ C > 0, ∃ t, … is trivially provable with C = 1. Take A = {1}: sumRep A n ≤ 1 for all n, since only n = 2 is represented, once. Any partition must put 1 into some piece P i, and then sumRep (P i) 2 = 1, which is not < 1. With t = 0 the union is empty and cannot equal A. So the formal statement does not capture the content of Nešetřil–Rödl, who show the answer is no for every C, nor Erdős's C = 3, 4 results. Small C are degenerate under the ordered-pair convolution. Simply switching to ∀ C > 0, ¬ ∃ t, … with the ordered sumRep does not fix it, because that is false at C = 3. Ordered count ≤ 3 means each b ∈ A is the middle of at most one progression a < b < c in A, so colouring greedily with b opposite a gives t = 2. A faithful version should count unordered pairs a ≤ b, as in Nešetřil–Rödl Theorem 2, and state ∀ C > 0, ¬ ∃ t, …, ideally even with t depending on A. See issue #6540 and PR #7704.

   </details>

19. `Erdos918.erdos_918.variants.eq_aleph_0.parts.i`: severity 4, essentially misformalized

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/918.lean](https://github.com/google-deepmind/formal-conjectures/blob/e750f777b32aeae464c01809e0d223dd62e99fab/FormalConjectures/ErdosProblems/918.lean)
   - **Commit:** [`e750f777b32a`](https://github.com/google-deepmind/formal-conjectures/commit/e750f777b32aeae464c01809e0d223dd62e99fab) (2026-10-15)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Erdos918-erdos_918-variants-eq_aleph_0-parts-i.json](audits/FormalConjectures/ErdosProblems/918/Erdos918-erdos_918-variants-eq_aleph_0-parts-i.json)

   This variant asserts that no graph on aleph_2 vertices with chromatic number aleph_2 has every INDUCED subgraph on aleph_1 vertices of chromatic number exactly aleph_0, and is tagged `@[category textbook]`, i.e. claimed to be a known result. The only justification in the sources (erdosproblems.com/918, crediting louisd) is for (not necessarily induced) subgraphs: an edgeless subgraph on aleph_1 vertices has chromatic number 1, so the '= aleph_0' version is trivially impossible. The file's own formalisation note concedes this argument does not carry over to induced subgraphs. For induced subgraphs the statement needs an aleph_1-set W whose induced chromatic number is finite or at least aleph_1. Under CH this follows from Erdős–Rado (aleph_2 -> (aleph_1)^2 gives an independent set or clique of size aleph_1), but without CH, aleph_2 -/-> (aleph_1)^2 is consistent (a Sierpiński-type colouring when 2^aleph_0 >= aleph_2), and then the statement appears entangled with the open main question erdos_918.parts.i. I found no source establishing the statement in ZFC, so the `textbook` label (and plausibly the provability of the statement in ZFC) is unsupported. Suggested fix: retag as open, or restrict the variant to the all-subgraphs form already stated as erdos_918.variants.eq_aleph_0_all_subgraphs.parts.i. The same concern applies to erdos_918.variants.eq_aleph_0.parts.ii.

   </details>

20. `FanelliMoscardelli.stability_threshold_tight`: severity 3, edge cases or discrepancies, but still equivalent

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/Paper/ApproximatelyStableMatching.lean](https://github.com/google-deepmind/formal-conjectures/blob/a919f7f47b836b766f378c2b1360b28168bbdd9d/FormalConjectures/Paper/ApproximatelyStableMatching.lean)
   - **Commit:** [`a919f7f47b83`](https://github.com/google-deepmind/formal-conjectures/commit/a919f7f47b836b766f378c2b1360b28168bbdd9d) (2026-11-13)
   - **Model:** claude-fable-5-2
   - **Audit file:** [FanelliMoscardelli-stability_threshold_tight.json](audits/FormalConjectures/Paper/ApproximatelyStableMatching/FanelliMoscardelli-stability_threshold_tight.json)

   Compared against A. Fanelli and L. Moscardelli, 'Approximately Stable Matching' (ECAI 2025, doi:10.3233/FAIA251234, open-access PDF), Sections 2 and 5. Model: agents rank neighbours and themselves with rank_i(i) = δ_i + 1 (single is worst); a matching is an involution with fixed points single; {i,j} ∈ E is k-blocking at m if rank_i(m(i)) − rank_i(j) ≥ k and rank_j(m(j)) − rank_j(i) ≥ k; k ≥ 1. Roommates.CompleteProfile/partnerRank/IsKBlockingPair/IsKStable with the complete graph ⊤ reproduce this exactly (one-based ranks, self ranked n), and stabilityThreshold N is the least k ≥ 1 such that every complete profile on N agents has a k-stable matching (existence is monotone in k, so this is the threshold). Section 5: 'Theorem 1 shows existence (and convergence) for k = ⌈|N|/2⌉ ... exhaustive search on all complete graphs with up to |N| = 6 nodes ... k = ⌈|N|/2⌉ − 1 does not suffice ... We conjecture that the lower bound can be improved and that ⌈|N|/2⌉ could represent the true threshold even for larger values of |N|.' The value (N+1)/2 in ℕ is ⌈N/2⌉, correct (the ceilings are confirmed by Theorem 2's k = ⌊(n−3)/2⌋ + 1 = ⌈n/2⌉ − 1). Discrepancy: the paper's conjecture reads as 'the threshold is ⌈|N|/2⌉ for every |N|' (verified by them for |N| ≤ 6, conjectured beyond), whereas the Lean statement only asserts it for all N ≥ N₀ for some unspecified N₀ (the extra conjunct 3 ≤ N₀ is vacuous, since N₀ can always be increased). The Lean statement is therefore a priori weaker than the conjecture (it would remain true if the formula failed at finitely many N ≥ 7); a proof of the Lean statement would not settle the conjecture as stated, though a disproof would refute it. A faithful version would be ∀ N, stabilityThreshold N = (N + 1) / 2 (true for N = 0? stabilityThreshold 0 = 1 ≠ 0, so ∀ N ≥ 1).

   </details>

21. `Erdos462.erdos_462`: severity 3, edge cases or discrepancies, but still equivalent

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/462.lean](https://github.com/google-deepmind/formal-conjectures/blob/da703a5f239f734a47ede2f4e99b9ccc9e644cb5/FormalConjectures/ErdosProblems/462.lean)
   - **Commit:** [`da703a5f239f`](https://github.com/google-deepmind/formal-conjectures/commit/da703a5f239f734a47ede2f4e99b9ccc9e644cb5) (2026-11-11)
   - **Model:** claude-fable-5-2
   - **Audit file:** [Erdos462-erdos_462.json](audits/FormalConjectures/ErdosProblems/462/Erdos462-erdos_462.json)

   Compared against erdosproblems.com/462, which states Σ_{n<x, n not prime} p(n)/n ~ c x^{1/2}/(log x)² and then asks whether there is C > 0 with Σ_{x≤n≤x+Cx^{1/2}(log x)²} p(n)/n ≫ 1 for all large x (p(n) the least prime factor). The Lean statement transcribes the second sum literally, over all n in [x, x + C√x(log x)²], including primes. Concrete discrepancy with the likely intent: for prime n, p(n)/n = 1, so the inclusive sum is ≥ 1 as soon as the window contains a prime; the statement therefore follows from prime-gap bounds of the form p_{k+1} − p_k ≪ √p_k (log p_k)² (e.g. under RH), and becomes a question mostly about primes in short intervals. The window length C√x(log x)² is exactly the scale at which the composite-only sum from the first sentence averages Θ(1) (its density is ≈ (c/2)x^{−1/2}(log x)^{−2}), strongly suggesting Erdős meant composite n here too. The composite-only version implies the Lean statement but not conversely. The website text is itself ambiguous, so the formalisation is defensible as a literal reading, but neither the docstring nor the statement addresses the issue, and the formal problem may be strictly easier than the intended one.

   </details>

22. `Erdos601.erdos_601.variants.omega_1_omega_plus_2`: severity 3, edge cases or discrepancies, but still equivalent

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/601.lean](https://github.com/google-deepmind/formal-conjectures/blob/da703a5f239f734a47ede2f4e99b9ccc9e644cb5/FormalConjectures/ErdosProblems/601.lean)
   - **Commit:** [`da703a5f239f`](https://github.com/google-deepmind/formal-conjectures/commit/da703a5f239f734a47ede2f4e99b9ccc9e644cb5) (2026-11-11)
   - **Model:** claude-fable-5-2
   - **Audit file:** [Erdos601-erdos_601-variants-omega_1_omega_plus_2.json](audits/FormalConjectures/ErdosProblems/601/Erdos601-erdos_601-variants-omega_1_omega_plus_2.json)

   Compared against erdosproblems.com/601 (for which limit ordinals α must every graph on α have an infinite path or an independent set of order type α? EHM70 proved it for α < ω₁^{ω+2}; Erdős offered $250 for 'showing what happens when α = ω₁^{ω+2}'; Larson proved it for all α < 2^ℵ₀ under Martin's Axiom) and the zbMATH/MaRDI review of Baumgartner–Larson, 'A diamond example of an ordinal graph with no infinite paths', Ann. Pure Appl. Logic (1990), which states that if Jensen's ◇ holds then α ↛ (ω₁^{ω+2}, infinite path)² for all α < ω₂. As a transcription, HasPathOrIndepSetOfType (ω_1 ^ (ω+2)) is accurate (an injective ℕ-sequence with consecutive adjacencies is a one-way infinite path; the independent set must have order type ω₁^{ω+2}). The discrepancy is in its status and documentation: taking α = ω₁^{ω+2} < ω₂ in Baumgartner–Larson, ◇ (true in L) refutes the statement, while MA + 2^ℵ₀ = ℵ₂ (where ω₁^{ω+2} < 2^ℵ₀) proves it by Larson's theorem. So the statement is independent of ZFC (and of Lean's foundations), and can be neither proved nor disproved. The theorem is nonetheless tagged 'research open' and its docstring says 'Erdős conjectured the positive answer'; neither the file nor the erdosproblems page mentions the Baumgartner–Larson result. The formula is a faithful reading of the question at ω₁^{ω+2}, but the problem's actual resolution (independence) cannot be reached through this statement, and the open categorisation is misleading. The same independence affects erdos_601.variants.universal, which ◇ refutes, so that one is not provable either.

   </details>

23. `Erdos918.erdos_918.variants.all_subgraphs.parts.i`: severity 3, edge cases or discrepancies, but still equivalent

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/918.lean](https://github.com/google-deepmind/formal-conjectures/blob/da703a5f239f734a47ede2f4e99b9ccc9e644cb5/FormalConjectures/ErdosProblems/918.lean)
   - **Commit:** [`da703a5f239f`](https://github.com/google-deepmind/formal-conjectures/commit/da703a5f239f734a47ede2f4e99b9ccc9e644cb5) (2026-11-11)
   - **Model:** claude-fable-5-2
   - **Audit file:** [Erdos918-erdos_918-variants-all_subgraphs-parts-i.json](audits/FormalConjectures/ErdosProblems/918/Erdos918-erdos_918-variants-all_subgraphs-parts-i.json)

   Compared against erdosproblems.com/918, first question: is there a graph on ℵ₂ vertices with chromatic number ℵ₂ such that every subgraph on ℵ₁ vertices has chromatic number ≤ ℵ₀? The Lean variant asserts ∃ V : Type u, G with #V = ℵ₂, chromaticCardinal G = ℵ₂, and every subgraph H with #H.verts = ℵ₁ having chromaticCardinal ≤ ℵ₀; as the file notes, for '≤ ℵ₀' this is equivalent to the induced-subgraph version erdos_918.parts.i. As a transcription this is accurate. The discrepancy is status: the set-theory literature (surfaced in my search, e.g. as summarised in discussions of the Erdős–Hajnal problem) records that Baumgartner (1984) showed it consistent with GCH that such a graph exists, while Foreman and Laver (1988) showed, relative to a huge cardinal, that it is consistent that every graph of size and chromatic number ℵ₂ has an ℵ₁-sized subgraph of chromatic number ℵ₁. If so, the statement is independent of ZFC (and cannot be proved or refuted in Lean, assuming huge cardinals are consistent), yet it is tagged 'research open' as an ordinary yes/no question, and neither the file nor the page mentions this. I am fairly but not fully certain of these citations (I did not read the original papers). Faithful formula; status/categorisation misleading.

   </details>

24. `Erdos887.erdos_887.parts.i`: severity 3, edge cases or discrepancies, but still equivalent

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/887.lean](https://github.com/google-deepmind/formal-conjectures/blob/2f91d251c07fbbaf9435166d47c11e884a08a6cf/FormalConjectures/ErdosProblems/887.lean)
   - **Commit:** [`2f91d251c07f`](https://github.com/google-deepmind/formal-conjectures/commit/2f91d251c07fbbaf9435166d47c11e884a08a6cf) (2026-11-09)
   - **Model:** claude-fable-5-2
   - **Audit file:** [Erdos887-erdos_887-parts-i.json](audits/FormalConjectures/ErdosProblems/887/Erdos887-erdos_887-parts-i.json)

   Compared against erdosproblems.com/887: 'Is there an absolute constant K such that, for every C>0, if n is sufficiently large then n has at most K divisors in (n^{1/2}, n^{1/2}+C n^{1/4})?' The counting is right: for natural d, ⌊√n⌋ < d < ⌈√n + C n^{1/4}⌉ is equivalent to √n < d < √n + C n^{1/4}, and the quantifier order (K before C, 'eventually in n' after C) matches. The discrepancy is in the framing: the site asks a yes/no existence question, which the file states correctly as `erdos_887.parts.ii` (∃ K, …), but this declaration recasts it as a `question value` with `erdos_887.parts.i.answer : ℕ := sorry` and the statement 'the divisor count is eventually ≤ answer'. That is not a question with a determined value: if any K works then every larger K also makes the statement true (the statement does not ask for the least K, so e.g. it does not capture Erdős–Rosenfeld's 'is 4 best possible?'), and if the answer to the site's question is 'no' then the statement is false for every value of the answer and the convention of 'fill in the answer and leave the statement unchanged' cannot record the resolution. Proving the statement for some value of the answer is nevertheless equivalent to an affirmative answer to the site's question, so it is a non-standard but not misleading formulation, essentially a duplicate of parts.ii with the witness pulled out.

   </details>

25. `Andrica.andrica_conjecture.ferreira_large_n`: severity 3, edge cases or discrepancies, but still equivalent

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/Wikipedia/Andrica.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/Wikipedia/Andrica.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Andrica-andrica_conjecture-ferreira_large_n.json](audits/FormalConjectures/Wikipedia/Andrica/Andrica-andrica_conjecture-ferreira_large_n.json)

   States Andrica's inequality for all sufficiently large n and tags it `research solved`, citing Ferreira, arXiv:2307.08725. That preprint (four versions 2023–2026, "submitted to Annals of Mathematics", no journal reference) claims an asymptotic count of primes in (x, x + x^λ] for every λ ∈ (0,1). That would vastly exceed the established short-interval results (exponent 7/12, Huxley/Heath-Brown). It is not an accepted result, and the abstract does not even mention Andrica's conjecture; it only claims Legendre's conjecture for large x. The eventual form of Andrica's conjecture (equivalent to p_{n+1} − p_n < 2√p_n + 1 eventually) is still open: the best unconditional gap bound is p^{0.525} (Baker–Harman–Pintz), and even RH gives only O(√p log p). The formal statement is fine as a weakening of Andrica, but the category should be `research open` and the attribution to Ferreira removed or qualified.

   </details>

26. `Brocard.brocard_conjecture.ferreira_large_n`: severity 3, edge cases or discrepancies, but still equivalent

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/Wikipedia/BrocardConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/Wikipedia/BrocardConjecture.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Brocard-brocard_conjecture-ferreira_large_n.json](audits/FormalConjectures/Wikipedia/BrocardConjecture/Brocard-brocard_conjecture-ferreira_large_n.json)

   States Brocard's conjecture for all large n, tagged `research solved` and attributed to Ferreira (arXiv:2307.08725). That is an unrefereed preprint claiming the prime number theorem in (x, x + x^λ] for every λ ∈ (0,1). This would far exceed established short-interval results, and it is not an accepted theorem. The eventual statement needs primes in intervals of length ≍ √x near x = p_n², which is beyond current knowledge (even Legendre's conjecture is open). The statement is fine as a weakening, but it should be tagged `research open` rather than solved.

   </details>

27. `Green29.green_29`: severity 3, edge cases or discrepancies, but still equivalent

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/GreensOpenProblems/29.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/GreensOpenProblems/29.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Green29-green_29.json](audits/FormalConjectures/GreensOpenProblems/29/Green29-green_29.json)

   Formalizes Green's Problem 29 literally: is there S ⊆ A with |S| ≫ K^{−O(1)}|A| and S⁸ ⊆ A⁴ for every K-approximate group A? It asserts the negative answer and is tagged solved, citing a counterexample A = ({−1}×H) ∪ ({1}×H) ∪ {(0,1)} in ℤ×H. I checked the counterexample. A is symmetric and contains 1. A² = {−2,…,2}×H ⊆ A ∪ (1,1)A ∪ (−1,1)A, so A is a 3-approximate group for every H. Any s = (±1, h) ∈ S has s⁸ with first coordinate ±8, outside A⁴ ⊆ {−4,…,4}×H, so S ⊆ A forces S ⊆ {(0,1)}. The counterexample is therefore valid, but it works only because of the literal containment S ⊆ A. If S may lie in A² (or anywhere, as in the known Sanders/Croot–Sisask result recorded in `green_29.variant`), then S = {0}×H has |S| ≈ |A|/2 and S⁸ ⊆ A⁴. The intended question, a polynomial-in-K version of Sanders' theorem, is untouched. So marking the problem "solved (negative)" most likely rests on a slip in the phrasing ("S ⊂ A") rather than resolving Green's problem. The formalization should either use the intended containment or note that the literal version is trivially false and the real question remains open.

   </details>

28. `LegendreConjecture.legendre_conjecture.ferreira_large_n`: severity 3, edge cases or discrepancies, but still equivalent

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/Wikipedia/LegendreConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/Wikipedia/LegendreConjecture.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5
   - **Audit file:** [LegendreConjecture-legendre_conjecture-ferreira_large_n.json](audits/FormalConjectures/Wikipedia/LegendreConjecture/LegendreConjecture-legendre_conjecture-ferreira_large_n.json)

   Legendre's conjecture for all large n, tagged `research solved` and attributed to Ferreira (arXiv:2307.08725). That preprint is unrefereed ("submitted to Annals") and claims asymptotics for primes in (x, x + x^λ] for every λ > 0. That would be far beyond the established short-interval results (λ > 7/12), and it is not an accepted result. The eventual Legendre statement remains open: it would need prime gaps O(√p), which is unknown even under RH. The category should be `research open`.

   </details>

29. `Oppermann.oppermann_conjecture.ferreira_large_x`: severity 3, edge cases or discrepancies, but still equivalent

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/Wikipedia/Oppermann.lean](https://github.com/google-deepmind/formal-conjectures/blob/7bdc4a42f24c0316f81c73b26121794b2bed96a3/FormalConjectures/Wikipedia/Oppermann.lean)
   - **Commit:** [`7bdc4a42f24c`](https://github.com/google-deepmind/formal-conjectures/commit/7bdc4a42f24c0316f81c73b26121794b2bed96a3) (2026-11-02)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Oppermann-oppermann_conjecture-ferreira_large_x.json](audits/FormalConjectures/Wikipedia/Oppermann/Oppermann-oppermann_conjecture-ferreira_large_x.json)

   Oppermann's conjecture for all large x, tagged `research solved` and attributed to Ferreira's unrefereed preprint arXiv:2307.08725. That preprint claims prime asymptotics in (x, x + x^λ] for all λ > 0, far beyond accepted results (λ > 7/12), and is not an accepted proof. Even eventual Oppermann requires primes in intervals of length ≈ √y near y, which is open (stronger than eventual Legendre). The statement is fine, but the category should be `research open`.

   </details>

30. `Bugeaud06.problem_10_6_variant_1`: severity 3, edge cases or discrepancies, but still equivalent

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean](https://github.com/google-deepmind/formal-conjectures/blob/d995ef5d306637c0a2e489c7e579647168d7df2f/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean)
   - **Commit:** [`d995ef5d3066`](https://github.com/google-deepmind/formal-conjectures/commit/d995ef5d306637c0a2e489c7e579647168d7df2f) (2026-11-01)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Bugeaud06-problem_10_6_variant_1.json](audits/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6/Bugeaud06-problem_10_6_variant_1.json)

   Problem 10.6 asks informally for a 'very rapidly increasing' sequence dense modulo one for every irrational ξ; Bugeaud's book text is paywalled and I compared with the file's docstring and Katz, arXiv:1607.00670. Katz describes very sparse universally densifying sequences in Corollary 4.10 and says this 'answers a question by Y. Bugeaud'. The discrepancy is that the Lean statement fixes one interpretation invented in the file, a ratio floor m_{n+1}/m_n≥1+c/log n, which the source does not state. The file itself admits several inequivalent readings. A proof of this implies a positive answer to the informal question, but its 'research open' status applies only to this reading, and the source question may be regarded as answered. A reasonable but non-canonical formalization.

   </details>

31. `Equidistribution.isAccumulationPoint_three_halves_pow`: severity 3, edge cases or discrepancies, but still equivalent

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/Books/UniformDistributionOfSequences/Equidistribution.lean](https://github.com/google-deepmind/formal-conjectures/blob/d995ef5d306637c0a2e489c7e579647168d7df2f/FormalConjectures/Books/UniformDistributionOfSequences/Equidistribution.lean)
   - **Commit:** [`d995ef5d3066`](https://github.com/google-deepmind/formal-conjectures/commit/d995ef5d306637c0a2e489c7e579647168d7df2f) (2026-11-01)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Equidistribution-isAccumulationPoint_three_halves_pow.json](audits/FormalConjectures/Books/UniformDistributionOfSequences/Equidistribution/Equidistribution-isAccumulationPoint_three_halves_pow.json)

   The docstring says 'Find an accumulation point of (3/2)ⁿ mod 1', research open, @[question value]. The format follows the value-question convention of upstream issue #6690 (def ….answer := sorry). Discrepancy: the statement is closed with no new mathematics by answer := Classical.choose of the file's own test theorem isAccumulationPoint_three_halves_pow_exists, and by the _infinite theorem it is satisfied by infinitely many values, so it does not pin down the explicit point the question wants. Upstream has treated statements closable by a degenerate or self-referential answer as misformalizations: #4977 (Erdős 40, answer closed by ∅, fixed), and #4923 lists reflexive answers for Erdős 422, 539 and 789 as open items. I could not find the source of the 'find' phrasing in the quoted Kuipers-Niederreiter text.

   </details>

32. `Erdos1000.erdos_1000`: severity 3, edge cases or discrepancies, but still equivalent

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/1000.lean](https://github.com/google-deepmind/formal-conjectures/blob/d995ef5d306637c0a2e489c7e579647168d7df2f/FormalConjectures/ErdosProblems/1000.lean)
   - **Commit:** [`d995ef5d3066`](https://github.com/google-deepmind/formal-conjectures/commit/d995ef5d306637c0a2e489c7e579647168d7df2f) (2026-11-01)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Erdos1000-erdos_1000.json](audits/FormalConjectures/ErdosProblems/1000/Erdos1000-erdos_1000.json)

   Compared with erdosproblems.com/1000, whose definition is that m/n_k 'does not have denominator n_j for j<k when written in lowest form; equivalently, n_k/(m,n_k)≠n_j'. Discrepancy: phiSeq instead requires n_k/(m,n_k) ∤ n_j, and the docstring states this divisibility as the page's equivalent form. These differ: for A={2,3,6} at n_k=6, m=6 has reduced denominator 1, which divides 2 but is not in A, so it counts on the page but not in Lean. Lean's count is therefore at most the page's, so a sequence with average →0 under the page's definition also works here, but not conversely a priori. The divisibility form is plausibly Cassels' intended 'new fractions' notion, but I could not read [Ca50b] or [Ha]. The rest (strictly increasing positive sequence, Cesàro average →0, existence claim) matches.

   </details>

33. `Erdos108.erdos_108`: severity 3, edge cases or discrepancies, but still equivalent

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/108.lean](https://github.com/google-deepmind/formal-conjectures/blob/d995ef5d306637c0a2e489c7e579647168d7df2f/FormalConjectures/ErdosProblems/108.lean)
   - **Commit:** [`d995ef5d3066`](https://github.com/google-deepmind/formal-conjectures/commit/d995ef5d306637c0a2e489c7e579647168d7df2f) (2026-11-01)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Erdos108-erdos_108.json](audits/FormalConjectures/ErdosProblems/108/Erdos108-erdos_108.json)

   The encoding faithfully transcribes the question on erdosproblems.com/108: for all r ≥ 4 and k ≥ 2 there is a finite f such that every graph with χ ≥ f has a subgraph with girth ≥ r and χ ≥ k. Mathlib's girth is ℕ∞-valued with acyclic = ⊤, and graphs of infinite chromatic number reduce to the finite case by de Bruijn–Erdős. However, the page now reports that the answer is negative for r ≥ 5. There are triangle-free graphs of arbitrarily large chromatic number all of whose C4-free subgraphs are 3-colourable, so f(k,r) is finite iff r ≤ 4 or k ∈ {1,2}. The universally quantified statement is therefore false (for example r = 5, k = 4) but is tagged `research open` and stated affirmatively. It should be negated and recategorised as solved, with the true r = 4 case (Rödl) given as a separate variant, as the file's TODO already suggests.

   </details>

34. `Erdos143.erdos_143.parts.ii`: severity 3, edge cases or discrepancies, but still equivalent

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/143.lean](https://github.com/google-deepmind/formal-conjectures/blob/d995ef5d306637c0a2e489c7e579647168d7df2f/FormalConjectures/ErdosProblems/143.lean)
   - **Commit:** [`d995ef5d3066`](https://github.com/google-deepmind/formal-conjectures/commit/d995ef5d306637c0a2e489c7e579647168d7df2f) (2026-11-01)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Erdos143-erdos_143-parts-ii.json](audits/FormalConjectures/ErdosProblems/143/Erdos143-erdos_143-parts-ii.json)

   Encodes the first question on the page, Σ_{x∈A} 1/(x log x) < ∞ for every well-separated A, in the affirmative and tagged `research open`. erdosproblems.com/143 now reports a formalised negative answer: some such A has Σ 1/(x log x) = ∞. The Lean statement is therefore false. It should be negated and recategorised as solved, ideally citing the formal counterexample.

   </details>

35. `Erdos29.erdos_29`: severity 3, edge cases or discrepancies, but still equivalent

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/29.lean](https://github.com/google-deepmind/formal-conjectures/blob/b6939a3a0d89e5f999fa8c6483a6ef646c1e2923/FormalConjectures/ErdosProblems/29.lean)
   - **Commit:** [`b6939a3a0d89`](https://github.com/google-deepmind/formal-conjectures/commit/b6939a3a0d89e5f999fa8c6483a6ef646c1e2923) (2026-10-30)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Erdos29-erdos_29.json](audits/FormalConjectures/ErdosProblems/29/Erdos29-erdos_29.json)

   Compared against erdosproblems.com/29: is there an EXPLICIT construction of A ⊆ ℕ with A + A = ℕ and 1_A∗1_A(n) = o(n^ε) for every ε > 0? The page stresses that existence was already proved by Erdős probabilistically and that this problem asks for a constructive solution. The Lean statement asserts only existence, ∃ A, A + A = univ ∧ ∀ ε > 0, sumRep =o n^ε, so it omits the explicitness that is the content of the question; a non-constructive proof would establish it without solving the problem. The docstring acknowledges this. The discrepancy does not change truth value, since JPSZ24 gives an explicit set, and explicitness is hard to state formally, so this is not a misformalization of provability, but the formal statement is strictly weaker than the question asked.

   </details>

36. `Erdos42.erdos_42.variants.constructive`: severity 3, edge cases or discrepancies, but still equivalent

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/42.lean](https://github.com/google-deepmind/formal-conjectures/blob/b6939a3a0d89e5f999fa8c6483a6ef646c1e2923/FormalConjectures/ErdosProblems/42.lean)
   - **Commit:** [`b6939a3a0d89`](https://github.com/google-deepmind/formal-conjectures/commit/b6939a3a0d89e5f999fa8c6483a6ef646c1e2923) (2026-10-30)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Erdos42-erdos_42-variants-constructive.json](audits/FormalConjectures/ErdosProblems/42/Erdos42-erdos_42-variants-constructive.json)

   Compared against erdosproblems.com/42, which has no constructive claim. The docstring promises 'explicit bounds' and a 'constructive function f', but the statement is ∃ f : ℕ → ℕ with the implication for N ≥ f(M). Lean's ∃ is non-constructive, and this is logically equivalent to `erdos_42`: take f(M) from each eventual threshold. So the formal statement does not capture what the docstring advertises; nothing about explicitness is encoded. The statement is true whenever the main one is, so provability is unaffected, but it is not a distinct variant as documented.

   </details>

37. `Erdos923.erdos_923`: severity 3, edge cases or discrepancies, but still equivalent

   <details>
   <summary>Details</summary>

   - **File:** [FormalConjectures/ErdosProblems/923.lean](https://github.com/google-deepmind/formal-conjectures/blob/e750f777b32aeae464c01809e0d223dd62e99fab/FormalConjectures/ErdosProblems/923.lean)
   - **Commit:** [`e750f777b32a`](https://github.com/google-deepmind/formal-conjectures/commit/e750f777b32aeae464c01809e0d223dd62e99fab) (2026-10-15)
   - **Model:** claude-opus-5-5
   - **Audit file:** [Erdos923-erdos_923.json](audits/FormalConjectures/ErdosProblems/923/Erdos923-erdos_923.json)

   Compared against erdosproblems.com/923: 'Is it true that, for every k, there is some f(k) such that if G has chromatic number >= f(k) then G contains a triangle-free subgraph with chromatic number >= k?' (yes, Rödl [Ro77]). In the statement, the source's k is `n` and f(k) is `k`, and the quantifiers are `∀ (V : Type*) (n : ℕ), ∃ k, ∀ G : SimpleGraph V, ...`: the threshold may depend on the vertex type V, whereas in the source f(k) is a single function uniform over all graphs. For finite V the statement is vacuous (take k > |V|, since `chromaticNumber : ℕ∞` is at most |V|). The formulation is still equivalent to the intended one: taking V = ℕ forces one threshold for all finite graphs (each embeds with isolated padding), and by de Bruijn–Erdős a graph on any V with χ >= that finite threshold has a finite subgraph with the same property, so the V = ℕ threshold works universally. Because equivalence needs this argument and the quantifier order differs from every usual formulation, I rate it 3. Suggested fix: move `∃ k` before `∀ V`, i.e. `∀ n, ∃ k, ∀ (V : Type*) (G : SimpleGraph V), ...`, which matches the source and is still what Rödl's theorem gives.

   </details>
