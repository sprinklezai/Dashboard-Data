import pandas as pd
import glob
import os

for xlsx in glob.glob("*.xlsx"):
    name = os.path.splitext(xlsx)[0]
    print(f"Converting {xlsx} ...")
    df = pd.read_excel(xlsx, header=3)
    for col in df.columns:
            df[col] = df[col].astype("string")
    df.to_parquet(name + ".parquet", compression="zstd")
    print(f"  Done: {len(df):,} rows -> {name}.parquet")

print("All files converted.")