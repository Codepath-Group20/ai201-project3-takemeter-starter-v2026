from datasets import load_dataset
import pandas as pd

# 1. Pull the IMDb dataset from Hugging Face
dataset = load_dataset("stanfordnlp/imdb")

# 2. Grab the first 200 rows from the training split
df = pd.DataFrame(dataset['train'][:200])

# The original dataset comes with labels: 0 for negative, 1 for positive.
# 3. Map those 0/1 integers to your custom taxonomy names, 
# or overwrite them with your own style labels.
# For example, if you want to map them to your own 3 labels:
def custom_label_mapping(row):
    # This is where you assign your own labels based on the text or original sentiment
    # Or you can manually loop/assign them.
    return "nuanced_critique" # placeholder logic

df['label'] = df.apply(custom_label_mapping, axis=1)

# 4. Create the 'note' column required by the project
df['note'] = "Imported from Hugging Face IMDb dataset and categorized."

# 5. Keep only the 3 required columns
df = df[['text', 'label', 'note']]

# 6. Save it locally into your data folder as a single CSV
df.to_csv("data/labels.csv", index=False)
print("Saved 200 rows to data/labels.csv!")
