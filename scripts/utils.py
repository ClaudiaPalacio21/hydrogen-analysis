import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def load_data(filepath):
    """Load a CSV file and return a summary."""
    import pandas as pd
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns")
    return df

def normalize(df, column):
    """Normalize a column to range 0-1."""
    df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    return df
