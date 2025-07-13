import polars as pl

# Prompt user for CSV file path or URL
csv_path = input("Enter path or URL to your CSV file: ").strip()

# Read CSV into Polars DataFrame
try:
    df = pl.read_csv(csv_path, infer_schema_length=1000)
    print("\n=== Dataset Loaded Successfully ===")
except Exception as e:
    print("Error loading CSV:", e)
    exit()

# Display all columns
print(f"\nColumns in dataset ({len(df.columns)} total):")
print(df.columns)

# Identify column types
numeric_cols = [col for col, dtype in zip(df.columns, df.dtypes) 
                if dtype in [pl.Float64, pl.Float32, pl.Int64, pl.Int32, pl.UInt32, pl.UInt64]]
categorical_cols = [col for col, dtype in zip(df.columns, df.dtypes) 
                   if dtype in [pl.Utf8, pl.Categorical, pl.Boolean]]

print(f"\nNumeric columns ({len(numeric_cols)}): {numeric_cols}")
print(f"Categorical columns ({len(categorical_cols)}): {categorical_cols}")

# Summarize numerical columns
if numeric_cols:
    print("\n=== Numerical Column Summary ===")
    
    # Display stats column by column for readability
    print(f"{'Column':<45} {'Count':<8} {'Mean':<12} {'Std':<12} {'Min':<12} {'Max':<12}")
    print("-" * 110)
    
    for col in numeric_cols:
        stats = df.select([
            pl.col(col).count().alias('count'),
            pl.col(col).mean().alias('mean'),
            pl.col(col).std().alias('std'),
            pl.col(col).min().alias('min'),
            pl.col(col).max().alias('max')
        ])
        
        count = stats.item(0, 'count')
        mean = stats.item(0, 'mean') if stats.item(0, 'mean') is not None else 0
        std = stats.item(0, 'std') if stats.item(0, 'std') is not None else 0
        min_val = stats.item(0, 'min') if stats.item(0, 'min') is not None else 0
        max_val = stats.item(0, 'max') if stats.item(0, 'max') is not None else 0
        
        print(f"{col:<45} {count:<8} {mean:<12.3f} {std:<12.3f} {min_val:<12.3f} {max_val:<12.3f}")
    
    print("\nColumn Sums:")
    for col in numeric_cols:
        col_sum = df.select(pl.col(col).sum()).item()
        print(f"{col}: {col_sum:,.2f}")
        
else:
    print("\nNo numerical columns found.")

# Summarize categorical columns
if categorical_cols:
    print("\n=== Categorical Column Summary ===")
    for col in categorical_cols:
        n_unique = df.select(pl.col(col).n_unique()).item()
        
        print(f"\nColumn: {col} ({n_unique} unique values)")
        
        try:
            # Get value counts
            value_counts = df.select(pl.col(col)).group_by(col).agg(
                pl.len().alias('count')
            ).sort('count', descending=True).head(10)
            
            print("Top values:")
            for i in range(min(10, value_counts.height)):
                value = value_counts.item(i, col)
                count = value_counts.item(i, 'count')
                print(f"  {value}: {count}")
                
        except Exception as e:
            print(f"Could not summarize column '{col}': {e}")
else:
    print("\nNo categorical columns found.")

# Dataset overview
print(f"\n=== Dataset Overview ===")
print(f"Shape: {df.height} rows × {len(df.columns)} columns")
print(f"Memory usage: {df.estimated_size('mb'):.2f} MB")

print("\n=== Polars Descriptive Summary Complete ===")