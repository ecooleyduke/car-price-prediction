import pandas as pd
from sklearn.model_selection import train_test_split

def load_raw_data(path):
    return pd.read_csv(path)

def preprocess(df, cfg):
    df = df.drop(columns=cfg["preprocessing"]["drop_columns"])
    return df

def split(df, cfg):
    target = cfg["preprocessing"]["target"]
    X = df.drop(target, axis=1)
    y = df[target]
    
    return train_test_split(
        X,
        y,
        test_size=cfg["training"]["test_size"],
        random_state=cfg["training"]["random_state"]
    )
