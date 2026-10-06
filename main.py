import os
import argparse
import logging

from reader import read_csv
from cleaner import clean_data
from writer import write_excel


logging.basicConfig(
    filename="converter.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def convert_csv_to_excel(input_file, output_file):
    try:
        logging.info(f"Starting conversion: {input_file}")

        print("Reading CSV file...")
        df = read_csv(input_file)

        print("Cleaning data...")
        df = clean_data(df)

        print("Exporting to Excel...")
        os.makedirs(
            os.path.dirname(output_file) or ".",
            exist_ok=True
        )

        write_excel(df, output_file)

        logging.info(f"Conversion successful: {output_file}")

        print("Conversion completed successfully!")

    except Exception as e:
        logging.error(f"Conversion failed: {e}")
        print(f"Error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert CSV file to cleaned Excel file"
    )

    parser.add_argument(
        "input",
        help="Input CSV file"
    )

    parser.add_argument(
        "output",
        help="Output Excel file"
    )

    args = parser.parse_args()

    convert_csv_to_excel(args.input, args.output)