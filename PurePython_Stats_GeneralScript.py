import csv
from collections import defaultdict, Counter

def is_number(s):
    try:
        float(s)
        return True
    except:
        return False

def main():
    file_path = input("Enter the path to your CSV file: ").strip()
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
        columns = reader.fieldnames

    for col in columns:
        col_vals = [row[col] for row in data]
        valid_nums = [float(v) for v in col_vals if is_number(v)]
        missing = sum(1 for v in col_vals if v == '' or v is None)
        percent_numeric = len(valid_nums) / (len(col_vals) - missing + 1e-9)
        if percent_numeric > 0.8:
            # Numeric column
            print(f"\nColumn: {col} (numeric)")
            print(f"  Min: {min(valid_nums)}")
            print(f"  Max: {max(valid_nums)}")
            print(f"  Mean: {sum(valid_nums)/len(valid_nums):.2f}")
            print(f"  Missing: {missing}")
        else:
            # Categorical column
            counter = Counter(col_vals)
            print(f"\nColumn: {col} (categorical/mixed)")
            print(f"  Unique: {len(counter)}")
            if counter:
                print(f"  Most common: {counter.most_common(1)[0][0]} ({counter.most_common(1)[0][1]} times)")
            print(f"  Missing: {missing}")

if __name__ == "__main__":
    main()
