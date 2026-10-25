import os
import pandas as pd

# Path to your local dataset cache or working file
data_path = os.path.join("data", "imdb_local_cache.csv") # or imdb_local_cache.csv

if os.path.exists(data_path):
    # Load just the first 50 rows using pandas directly
    df = pd.read_csv(data_path, nrows=50)
    
    # Save a dedicated 50-sample subset if needed
    output_path = os.path.join("data", "fifty_sample.csv")
    df.to_csv(output_path, index=False)
    
    print(f"Successfully loaded and saved 50 samples to {output_path}")
    print(df.head())
else:
    print(f"Dataset not found at {data_path}. Please check your data directory.")
