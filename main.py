import argparse
import pandas as pd


def parse_args():
    parser = argparse.ArgumentParser(description="Clean a CSV dataset")
    parser.add_argument("--input", required=True, help="Path to input CSV")
    parser.add_argument("--output", required=True, help="Path to save cleaned CSV")

    parser.add_argument("--report", action="store_true", help="Print dataset summary report")
    parser.add_argument("--remove-duplicates", action="store_true", help="Remove duplicate rows")   
    parser.add_argument("--trim-whitespace", action="store_true", help="Trim leading and trailing spaces from text columns")
    return parser.parse_args()

    
def print_report(df):
    print("\nDataset Summary")
    print("----------------")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\nColumn Names")
    print("----------------")
    for column in df.columns:
        print(f"- {column}")

    print("\nMissing Values")
    print("----------------")
    print(df.isna().sum())

    print("\nDuplicate Rows")
    print("----------------")
    print(df.duplicated().sum())

    print("\nColumn Types")
    print("----------------")
    print(df.dtypes)
 

def main():
    args = parse_args()

    df = pd.read_csv(args.input)
    
    duplicates_before = 0

    if args.trim_whitespace:
        for column in df.select_dtypes(include=["object"]).columns:
            df[column] = df[column].apply(lambda x: x.strip() if isinstance(x, str) else x)
        print("\nTrimmed whitespace from text columns")

    if args.remove_duplicates:
        duplicates_before = df.duplicated().sum()
        df = df.drop_duplicates()

    if args.report:
        print_report(df)



    


    df.to_csv(args.output, index=False)


    print(f"Loaded {args.input}")
    print(f"Saved copy to {args.output}")
    print(f"Removed {duplicates_before} duplicate rows")




if __name__ == "__main__":
    main()