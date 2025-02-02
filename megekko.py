import re

from utils import *


def is_valid_link(link: str) -> bool:
    """
    TODO manage potential trailing "/" ?
    TODO re
    """
    return (link.startswith("https://www.megekko.nl/Computer/Componenten/")
            and (link.endswith("_d-list_cf-")
                 or link.endswith("_d-block_cf-")))

def get_n_pages(link: str) -> int:
    """
    get number of pages of a product category list
    """
    soup = get_soup(link)
    data_navpage_select = soup.find("select", {"data-navpage": ""})
    options = data_navpage_select.find_all("option")
    return len(options)

def category_function_selection(link: str):
    selected_category_function = None
    link_id_function_mapping = {  # automatic category detection
        "Hard-disks": storage,
        "SSD-Solid-state-drive-": storage,
        "Processoren": cpu,
        "Videokaarten": gpu
    }
    for link_id, function in link_id_function_mapping.items():
        if link_id in link:
            selected_category_function = function
            print(f"category ({selected_category_function.__name__}) detected in URL".upper())
            break
    if not selected_category_function:  # manual category selection
        selection_function_mapping = {
            "1": storage,
            "2": gpu,
            "3": cpu,
        }
        for selection, function in selection_function_mapping.items():
            print(f"{selection}: {function.__name__}")
        selected_category_function = selection_function_mapping.get(
            input("select category: "))

    return selected_category_function


def storage(product_divs):
    """
    TODO title, brand, capacity, price, url
    TODO search for capacity in both title and production information summary
    """
    product_datas = []
    for product_div in product_divs:
        title = product_div.find("meta", {"itemprop": "name"})["content"]
        url = product_div.find("meta", {"itemprop": "url"})["content"]
        price = product_div.find("meta", {"itemprop": "price"})["content"]
        product_datas.append({"title": title, "url": url, "price": price})

    for product_data in product_datas:
        print(product_data)

def cpu(products_data: list[dict[str, str]]):
    pass

def gpu(products_data: list[dict[str, str]]):
    pass


def main(link: str):
    """
    """
    # change to list view if not already, to show product information summary
    link = link.replace("_d-block_cf-", "_d-list_cf-")

    # megekko will redirect to closest valid page when page number
    # is out of range, and thus return status code 200
    product_divs = []
    n_pages = get_n_pages(link)
    print(n_pages)
    for n in range(1, n_pages + 1):
        current_page_link = re.sub(r"_p-\d+", f"_p-{n}", link)
        soup = get_soup(current_page_link)
        current_page_product_divs = soup.find_all(
            "div", itemtype="http://schema.org/Product")
        product_divs.extend(current_page_product_divs)

    selected_category_function = category_function_selection(link)
    if selected_category_function:
        selected_category_function(product_divs)
    else:
        print("CATEGORY NOT FOUND")
        exit(1)


if __name__ == "__main__":
    link = input("URL: ")
    if is_valid_link(link):
        main(link)
    else:
        print("INVALID URL")
        exit(1)
