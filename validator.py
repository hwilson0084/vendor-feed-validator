import pandas as pd

df = pd.read_csv("sample_vendor_feed.csv")

errors = []

for _, row in df.iterrows():

    if pd.isna(row["UPC"]):
        errors.append({
            "SKU": row["SKU"],
            "Error": "Missing UPC"
        })

    if pd.isna(row["Price"]):
        errors.append({
            "SKU": row["SKU"],
            "Error": "Missing Price"
        })
    if pd.isna(row["Description"]):
        errors.append({
            "SKU": row["SKU"],
            "Error": "Missing Description"
        })
results = pd.DataFrame(errors)

results.to_csv("exception_report.csv", index=False)

print(results)
print("Validation complete")
