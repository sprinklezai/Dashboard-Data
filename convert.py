import pandas as pd
import glob
import os

for xlsx in glob.glob("*.xlsx"):
    name = os.path.splitext(xlsx)[0]
    print(f"Converting {xlsx} ...")
    df = pd.read_excel(xlsx, header=3)
    df.to_csv(name + ".csv", index=False)
    print(f"  Done: {len(df):,} rows -> {name}.csv")

print("All files converted.")