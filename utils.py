import re


def extract_capacity(text):
    match = re.search(r'\b(\d+)\s?(TB|GB)\b', text)
    if not match:
        return ""

    capacity = float(match.group(1))
    unit = match.group(2)

    return str(capacity / 1000) if unit == "GB" else str(capacity)
