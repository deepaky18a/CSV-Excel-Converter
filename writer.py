import pandas as pd


def write_excel(df, output_path):
    try:
        df.to_excel(output_path, index=False)
        print(f"Excel file created successfully: {output_path}")

    except Exception as e:
        raise Exception(f"Error writing Excel file: {e}")