# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---

## 1. Overall Accuracy

**Criterion:** The model achieves an overall classification accuracy of at least 0.65 across the held-out test split, evaluated consistently across all three training seeds.

**Why this target:** With three balanced labels, a random guesser sits around 0.33 accuracy. A threshold of 0.65 doubles random performance and ensures the model is capturing meaningful patterns in IMDb writing styles rather than just guessing the majority class.

---

## 2. Per-Label Performance (Minority Class F1)

**Criterion:** The smallest label, `factual_summary_recap` (approx. 65 examples), achieves a minimum F1-score of 0.50 on the held-out test set.

**Why this target:** Because `factual_summary_recap` has fewer samples, only a small handful land in the test split per seed, making its score naturally jumpy. Setting 0.50 accounts for this sample variance while still demanding that the model doesn't completely ignore the class.

---

## 3. Per-Label Performance (Majority Class F1)

**Criterion:** The largest label, `nuanced_critique` (approx. 70 examples), achieves a minimum F1-score of 0.65 across all evaluation seeds.

**Why this target:** Since this is our most frequent category and features distinct technical/balanced keywords, the model has more training signal to learn from, so a higher F1 bar of 0.65 is expected to ensure reliable detection.

---

## 4. Class Balance / Distribution Guardrail

**Criterion:** The ratio between the most frequent predicted label and the least frequent predicted label on the test set does not exceed 2.0 to 1.

**Why this target:** Our training labels are tightly balanced (~70, ~65, ~65). If the model's predictions skew heavily toward one class, it indicates a collapse or severe bias rather than a true reflection of the underlying IMDb review taxonomy.

---

## 5. Confidence Calibration

**Criterion:** Predictions made with high model confidence (probability greater than 0.80) achieve an accuracy of at least 0.80.

**Why this target:** A trustworthy classifier should be more accurate when it is certain. If high-confidence predictions are frequently wrong, the model's internal probability calibration is untrustworthy for practical deployment.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
