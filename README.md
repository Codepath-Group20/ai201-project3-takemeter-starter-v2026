# TakeMeter Project: Social Media Post Classifier

## Overview
TakeMeter is a text classification pipeline built using **DistilBERT** (`distilbert-base-uncased`) to automatically categorize community discussion posts into a custom 3-label taxonomy.

---

## Taxonomy
Our custom classification taxonomy consists of three distinct classes:
1. **`nuanced_critique`**: Balanced, thoughtful posts that analyze both the strengths and weaknesses of a topic.
2. **`blind_hype_or_rant`**: Unnuanced expressions of extreme enthusiasm or frustration without deeper backing.
3. **`factual_summary_recap`**: Objective summaries, recaps, or reporting of events without heavy editorializing.

---

## Milestone Architecture
* **Base Model**: `distilbert-base-uncased` (Fine-tuned via Hugging Face `Trainer`)
* **Input Representation**: Tokenized text sequences padded/truncated to `max_length = 128`
* **Hardware Environment**: CPU-only execution (`PyTorch 2.14.1+cpu`)
* **Hyperparameters**:
  * Learning Rate: $2 \times 10^{-5}$
  * Batch Size: $16$
  * Epochs: $3$

---

## Milestone 5: Training Results & Three-Seed Evaluation

We evaluated our model across three random seeds (`42`, `7`, and `2024`) to measure training stability and performance variance on our test split ($N = 30$).

### Multi-Seed Comparison Table

| Measure | Seed 42[cite: 2] | Seed 7[cite: 2] | Seed 2024[cite: 2] | Spread[cite: 2] |
|---|---|---|---|---|
| **Overall accuracy**[cite: 2] | 1.000[cite: 2] | 1.000[cite: 2] | 1.000[cite: 2] | 0.000[cite: 2] |
| **Macro F1**[cite: 2] | 1.000[cite: 2] | 1.000[cite: 2] | 1.000[cite: 2] | 0.000[cite: 2] |
| **F1 — `nuanced_critique`**[cite: 2] | 1.000[cite: 2] | 1.000[cite: 2] | 1.000[cite: 2] | 0.000[cite: 2] |
| **F1 — `blind_hype_or_rant`**[cite: 2] | 1.000[cite: 2] | 1.000[cite: 2] | 1.000[cite: 2] | 0.000[cite: 2] |
| **F1 — `factual_summary_recap`**[cite: 2] | 1.000[cite: 2] | 1.000[cite: 2] | 1.000[cite: 2] | 0.000[cite: 2] |

*Accuracy moved 0.000 across seeds, indicating high stability for the current dataset split[cite: 2].*

### Aggregate Confusion Matrix (Test Split)

| True \ Predicted | `nuanced_critique`[cite: 2] | `blind_hype_or_rant`[cite: 2] | `factual_summary_recap`[cite: 2] |
|---|---|---|---|
| **`nuanced_critique`**[cite: 2] | 10[cite: 2] | 0[cite: 2] | 0[cite: 2] |
| **`blind_hype_or_rant`**[cite: 2] | 0[cite: 2] | 10[cite: 2] | 0[cite: 2] |
| **`factual_summary_recap`**[cite: 2] | 0[cite: 2] | 0[cite: 2] | 10[cite: 2] |

---

## Reproducibility & Artifacts
* **`results.json`**: Contains detailed evaluation metrics, classification reports, and confidence scoring for the primary run.
* **`results_three_seeds_before.json`**: Contains multi-seed evaluation metrics across seeds 42, 7, and 2024[cite: 2].
* **`test_split.csv`**: Saved test partition used for final model scoring and validation.
