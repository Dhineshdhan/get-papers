import csv
from typing import List, Dict

def write_csv(filename: str, data: List[Dict]):
    if not data:
        print("⚠️ No non-academic authors found. CSV not created.")
        return

    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
