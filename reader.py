import pandas as pd


def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df

    except FileNotFoundError:
        raise FileNotFoundError(
            f"CSV file not found: {file_path}"
        )

    except Exception as e:
        raise Exception(
            f"Error reading CSV file: {e}"
        )