import pandas as pd
from datasets import load_dataset

# Stream just 50 reviews from IMDb
dataset = load_dataset("imdb", split="train", streaming=True)
small_sample = list(dataset.take(50))

# Convert to DataFrame
df = pd.DataFrame(small_sample)
print(df.head())
