import csv
from typing import List, Dict

def write_csv(filename: str, data: List[Dict]):
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
