# IMDb Review Style Classifier (TakeMeter)

## 1. Overview
This project classifies IMDb user reviews based on **writing style and user intent** rather than traditional movie genres. By categorizing reviews into distinct stylistic buckets, we can better understand how different users articulate their thoughts on cinema.

## 2. Dataset & Community
* **Source Community:** [IMDb User Reviews](https://www.imdb.com/)
* **File Location:** `data/labels.csv`
* **Size:** 200 manually formatted and verified rows.

## 3. Custom Taxonomy
Our taxonomy breaks down reviews into three distinct styles to ensure clear boundaries and avoid class imbalance (ensuring no single label exceeds 70% of the dataset):

* **`nuanced_critique`**
  * *Definition:* A thoughtful, balanced review that weighs both positive and negative aspects of the film with specific examples (e.g., separating praise for cinematography from criticism of pacing or script).
* **`blind_hype_or_rant`**
  * *Definition:* An extreme emotional review that is either purely gushing praise or furious hatred without much balanced analysis or technical breakdown.
* **`factual_summary_recap`**
  * *Definition:* A review that focuses primarily on summarizing the plot sequence or narrative setup rather than offering a personal value judgment or critique.

## 4. Decision Rules & Hard Boundaries
* **Nuanced Critique vs. Blind Hype:** If a review expresses strong emotion (positive or negative) *without* qualifying it with secondary considerations (e.g., praising the acting while criticizing the script), it belongs in `blind_hype_or_rant`.
* **Factual Summary vs. Critique:** If a review spends more than 50% of its text describing plot beats, character movements, or backstory synopsis without evaluating quality, it must be labeled `factual_summary_recap`, even if the user provides a star rating.

---

## 5. Milestone 2: Refined Label Definitions & Examples

### Label 1: `nuanced_critique`
* **Definition:** A thoughtful, balanced review that weighs both positive and negative aspects of a film while grounding its critique in specific technical elements (e.g., acting, pacing, or cinematography).
* **Example 1:** "While the cinematography and lighting were genuinely breathtaking, the third-act pacing completely fell apart and ruined the character arcs."
* **Example 2:** "The lead actor delivered a career-best performance, though the supporting cast felt wooden and uninspired."

### Label 2: `blind_hype_or_rant`
* **Definition:** An extreme emotional review featuring pure gushing praise or furious hatred without structural balance or deep technical analysis.
* **Example 1:** "Absolute masterpiece! A timeless classic that everyone needs to watch immediately. 10/10!"
* **Example 2:** "Worst movie ever made. Total trash that wasted two hours of my life. Avoid at all costs!"

### Label 3: `factual_summary_recap`
* **Definition:** A review that focuses primarily on summarizing plot progression, setting, or narrative events without offering subjective value judgments.
* **Example 1:** "The film opens with a high-stakes bank robbery before flashing back to explain how the crew assembled over three years."
* **Example 2:** "Set in a dystopian future, society is divided into rigid factions until a young rebel discovers a hidden truth about the government."

---

## 6. Borderline Case & Decision Rule
* **Borderline Post:** *"The movie started with a robbery sequence and had terrible pacing in the second half."*
* **Competing Labels:** `factual_summary_recap` vs. `nuanced_critique`
* **Decision Rule:** If the post evaluates quality or expresses a critical judgment (e.g., "terrible pacing"), it is classified as `nuanced_critique`, even if it mentions a factual plot element like an opening sequence.

---

## 7. Milestone 4: Hard Cases & Labeling Workflow

### Labeling Workflow Disclosure
* **Cold-Labeled Set:** The first 20 rows of `data/labels.csv` were labeled entirely cold without assistant tools to establish a baseline honesty check and human agreement standard.
* **Assisted Set:** Rows 21 through 200 were pre-labeled via structured taxonomy templates and meticulously reviewed row-by-row to prevent noise and ensure class balance.
* **Class Balance Check:** All labels remain well under the 70% threshold ceiling (`nuanced_critique` ~35%, `blind_hype_or_rant` ~32.5%, `factual_summary_recap` ~32.5%).

### Hard Cases Documented During Labeling
1. **Hard Case 1**
   * **Post Text:** *"The movie started with an incredible heist sequence, but the dialogue felt like a poorly written high school play."*
   * **Competing Labels:** `nuanced_critique` vs. `factual_summary_recap`
   * **Choice & Rationale:** Chosen as `nuanced_critique` because despite mentioning an opening plot event (heist), the primary weight of the sentence evaluates artistic quality ("poorly written high school play").

2. **Hard Case 2**
   * **Post Text:** *"Absolute garbage waste of two hours, though the score by Hans Zimmer was decent."*
   * **Competing Labels:** `blind_hype_or_rant` vs. `nuanced_critique`
   * **Choice & Rationale:** Chosen as `blind_hype_or_rant`. Even though it makes a minor nod to the musical score, the overwhelming tone is an aggressive hostile rant without balanced structural critique.

3. **Hard Case 3**
   * **Post Text:** *"Set in 1944 Paris, the film follows an undercover spy trying to decode a radio transmission before midnight."*
   * **Competing Labels:** `factual_summary_recap` vs. `nuanced_critique`
   * **Choice & Rationale:** Chosen as `factual_summary_recap` because it remains entirely descriptive of the plot setting and narrative stakes without expressing praise, criticism, or emotional judgment.
