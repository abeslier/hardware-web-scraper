import re
import csv


def extract_capacity(text):
    """
    """
    match = re.search(r'\b(\d+)\s?(TB|GB)\b', text)
    if not match:
        return ""

    capacity = float(match.group(1))
    unit = match.group(2)

    return str(capacity / 1000) if unit == "GB" else str(capacity)

def export_csv(data: list[dict], file_path: str = "export.csv") -> str:
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    return file_path

def print_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        for row in reader:
            for field in header:
                print(f"{field}: {row[field]}")
            print()
