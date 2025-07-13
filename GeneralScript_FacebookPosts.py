# pandas_stats.py

import pandas as pd
import ast

def try_parse(value):
    if isinstance(value, str):
        try:
            return ast.literal_eval(value)
        except (ValueError, SyntaxError):
            return value
    return value

def describe_dataframe(df):
    print("\n=== Numeric Columns Summary ===")
    numeric_cols = df.select_dtypes(include="number").columns
    if len(numeric_cols) > 0:
        desc = df[numeric_cols].describe().T
        print(desc.applymap(lambda x: f"{x:.3f}"))
    else:
        print("No numeric columns found.")

    print("\n=== Categorical Columns Summary ===")
    cat_cols = df.select_dtypes(include="object").columns
    for col in cat_cols:
        print(f"\n--- {col} ---")
        try:
            parsed_col = df[col].map(try_parse)
            first_val = parsed_col.dropna().iloc[0] if not parsed_col.dropna().empty else None
            if isinstance(first_val, (list, dict)):
                print("Complex data (list/dict); summary skipped.")
                continue
        except Exception:
            parsed_col = df[col]
        mode = parsed_col.mode()
        print("Mode:", mode.iloc[0] if not mode.empty else "None")
        print("Unique:", parsed_col.nunique())
        print("Top 3:", parsed_col.value_counts().head(3).to_dict())

def main():
    csv_file = input("Enter path or URL to CSV file: ").strip()
    print(f"Loading: {csv_file}")
    try:
        df = pd.read_csv(csv_file)
        print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
        describe_dataframe(df)
    except Exception as e:
        print(f"Error loading file: {e}")

if __name__ == "__main__":
    main()

