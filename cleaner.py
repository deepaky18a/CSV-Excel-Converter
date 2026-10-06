import pandas as pd


def clean_data(df):
    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Remove extra spaces from text columns
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.strip()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Handle missing values
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].fillna("")
        else:
            df[column] = df[column].fillna(0)

    return df