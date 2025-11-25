import os
import pandas as pd
from utils import load_config


def download_data(url: str):
    df = pd.read_csv(url)
    return df


def save_data(df: pd.DataFrame, output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)


def main():
    config = load_config()

    data_cfg = config["data"]
    url = data_cfg["url"]
    output_dir = data_cfg["output_dir"]
    output_file = data_cfg["output_file"]

    # Build full local path
    output_path = os.path.join(output_dir, output_file)

    # Download + save
    df = download_data(url)
    save_data(df, output_path)

    print("Data ingestion complete")


if __name__ == "__main__":
    main()
