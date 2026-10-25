import os
import pandas as pd

class MockDataset:
    """Mimics a Hugging Face Dataset object using Pandas under the hood."""
    def __init__(self, df):
        self.df = df.reset_index(drop=True)
    
    def __len__(self):
        return len(self.df)
    
    def __getitem__(self, idx):
        if isinstance(idx, slice):
            sub_df = self.df.iloc[idx]
            return {
                'text': sub_df['text'].tolist(),
                'label': sub_df['label'].tolist()
            }
        row = self.df.iloc[idx]
        return {
            'text': row['text'],
            'label': int(row['label'])
        }
    
    def __iter__(self):
        for _, row in self.df.iterrows():
            yield {'text': row['text'], 'label': int(row['label'])}

class MockDatasetDict(dict):
    """Mimics a Hugging Face DatasetDict object."""
    pass

def load_dataset(name, *args, **kwargs):
    """
    Drop-in replacement for huggingface_hub's load_dataset('imdb') 
    that runs purely on Pandas and standard Python without requiring pyarrow.
    """
    if name != "imdb":
        raise ValueError(f"Mock load_dataset currently only supports 'imdb', got '{name}'")
    
    cache_file = "data/imdb_local_cache.csv"
    
    # Download and cache locally if it doesn't exist yet
    if not os.path.exists(cache_file):
        print("Downloading IMDB dataset CSV from reliable source...")
        url = "https://huggingface.co/datasets/scikit-learn/imdb/resolve/main/IMDB%20Dataset.csv"
        df = pd.read_csv(url)
        
        # Format columns: review -> text, sentiment -> label (1 for positive, 0 for negative)
        if 'review' in df.columns and 'sentiment' in df.columns:
            df['text'] = df['review']
            df['label'] = df['sentiment'].apply(lambda x: 1 if str(x).lower() == 'positive' else 0)
            df = df[['text', 'label']]
            
        df.to_csv(cache_file, index=False)
    else:
        print("Loading IMDB dataset from local cache...")
        df = pd.read_csv(cache_file)
    
    # Split into standard train (40k) and test (10k) splits
    train_df = df.iloc[:40000].reset_index(drop=True)
    test_df = df.iloc[40000:].reset_index(drop=True)
    
    return MockDatasetDict({
        'train': MockDataset(train_df),
        'test': MockDataset(test_df)
    })

if __name__ == "__main__":
    print("Testing custom load_dataset('imdb')...")
    dataset = load_dataset("imdb")
    
    print(f"Training samples: {len(dataset['train'])}")
    print(f"Test samples: {len(dataset['test'])}")
    
    # Print a quick sample
    sample = dataset['train'][0]
    print("\nSample Data Inspection:")
    print(f"Text snippet: {sample['text'][:100]}...")
    print(f"Label: {sample['label']}")
