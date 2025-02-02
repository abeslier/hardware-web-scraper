import requests
from bs4 import BeautifulSoup
import re


def get_soup(link: str) -> BeautifulSoup:
    response = requests.get(link)
    return BeautifulSoup(response.text, "html.parser")

def extract_capacity(text):
    match = re.search(r'\b(\d+)\s?(TB|GB)\b', text)
    if not match:
        return ""

    capacity = float(match.group(1))
    unit = match.group(2)

    return str(capacity / 1000) if unit == "GB" else str(capacity)

def print_table(data: list[dict], columns: list[str] = None):
    # use specified columns or all available keys if None
    headers = columns if columns else list(data[0].keys())
    
    # find maximum width for each column
    col_widths = {header: max(len(header), max(len(str(row.get(header, ''))) for row in data)) for header in headers}
    
    # create table border
    border = "+" + "+".join("-" * (col_widths[header] + 2) for header in headers) + "+"
    
    # print headers
    print(border)
    header_row = " | ".join(header.ljust(col_widths[header]) for header in headers)
    print(f"| {header_row} |")
    print(border)
    
    # print data rows
    for row in data:
        print(f"| {' | '.join(str(row.get(header, '')).ljust(col_widths[header]) for header in headers)} |")
    print(border)
