import argparse
import pandas as pd


def parse_args():
    parser = argparse.ArgumentParser(description="Clean a CSV dataset")
    parser.add_argument("--input", required=True, help="Path to input CSV")
    parser.add_argument("--output", required=True, help="Path to save cleaned CSV")
    return parser.parse_args()


def main():
    args = parse_args()

    df = pd.read_csv(args.input)
    df.to_csv(args.output, index=False)

    print(f"Loaded {args.input}")
    print(f"Saved copy to {args.output}")
    print(f"Rows: {len(df)}, Columns: {len(df.columns)}")


if __name__ == "__main__":
    main()