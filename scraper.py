import requests
from bs4 import BeautifulSoup

from utils import extract_capacity


def storage(products_data: list[dict[str, str]]):
    for product_data in products_data:
        print(extract_capacity(product_data["title"]))

def cpu(products_data: list[dict[str, str]]):
    pass

def gpu(products_data: list[dict[str, str]]):
    pass


def megekko_scraper(URL: str):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    
    products_divs = soup.find_all("div", itemtype="http://schema.org/Product")
    
    products_data = []
    for product_div in products_divs:
        title = product_div.find("meta", {"itemprop": "name"})["content"]
        url = product_div.find("meta", {"itemprop": "url"})["content"]
        price = product_div.find("meta", {"itemprop": "price"})["content"]
        products_data.append({"title": title, "url": url, "price": price})

    f = None  # category function
    
    # automatic category detection
    categories = {
        "Hard-disks": storage,
        "SSD-Solid-state-drive-": storage,
        "Processoren": cpu,
        "Videokaarten": gpu
    }
    for key, value in categories.items():
        if key in URL:
            print(f"category ({value.__name__}) automatically detected in URL".upper())
            f = value
            break

    # manual category selection
    if not f:
        categories = {
            "1": storage,
            "2": gpu,
            "3": cpu,
        }
        for key, value in categories.items():
            print(f"{key}: {value.__name__}")
        f = categories.get(input("select category: "))
    
    f(products_data) if f else exit(1)


if __name__ == "__main__":
    URL = input("URL: ")
    if URL.startswith("https://www.megekko.nl/Computer/Componenten/"):
        megekko_scraper(URL)
