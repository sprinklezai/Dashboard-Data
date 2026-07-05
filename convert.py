import pandas as pd
import glob
import os

CHUNK = 200000

for xlsx in glob.glob("*.xlsx"):
    name = os.path.splitext(xlsx)[0]
    print(f"Converting {xlsx} ...")
    df = pd.read_excel(xlsx, header=3)
    if len(df) <= CHUNK:
        df.to_csv(name + ".csv", index=False)
        print(f"  Done: {len(df):,} rows -> {name}.csv")
    else:
        for i in range(0, len(df), CHUNK):
            part = i // CHUNK + 1
            df.iloc[i:i+CHUNK].to_csv(f"{name}_part{part}.csv", index=False)
            print(f"  Done: part {part} -> {name}_part{part}.csv")

print("All files converted.")