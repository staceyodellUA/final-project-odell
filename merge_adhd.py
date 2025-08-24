import pandas as pd, glob, os

# If your CSVs are directly in "OBF-Psychiatric Dataset", use:
pattern = os.path.join("OBF-Psychiatric Dataset", "*.csv")

# If they’re in a subfolder named "ADHD", uncomment the next line and comment out the one above:
# pattern = os.path.join("OBF-Psychiatric Dataset", "ADHD", "*.csv")

files = glob.glob(pattern)
print("Found", len(files), "files:", files)

dfs = []
for f in files:
    df = pd.read_csv(f)
    df["subject_id"] = os.path.splitext(os.path.basename(f))[0]
    dfs.append(df)

combined = pd.concat(dfs, ignore_index=True)
os.makedirs("data", exist_ok=True)
combined.to_csv("data/ADHD_combined.csv", index=False)
print("Saved data/ADHD_combined.csv with", combined.shape[0], "rows")