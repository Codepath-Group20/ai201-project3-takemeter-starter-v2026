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
