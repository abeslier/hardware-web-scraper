import re, sys

from website import Website


class Megekko(Website):
    VALID_URL_RE = r"^(https://www\.megekko\.nl/Computer/Componenten/).*(_d-list_cf-|_d-block_cf-)$"
    wanted_data = {
        "title": "name",
        "url": "url",
        "price": "price",
    }

    def __init__(self, url: str):
        if not self.is_valid_url(url, self.VALID_URL_RE):
            sys.exit("INVALID URL")
        self.url = url.replace("_d-block_cf-", "_d-list_cf-")  # list view if not already (to show product info summary) 

        self.total_pages = self.get_total_pages()
        self.product_category_function = self.get_product_category_function()
        self.extracted_products_divs = self.extract_products_divs()
        self.extracted_products_data = self.extract_products_data(self.extracted_products_divs, self.wanted_data)

    def get_total_pages(self) -> int:
        soup = self.get_soup(self.url)
        data_navpage_select = soup.find("select", {"data-navpage": ""})
        options = data_navpage_select.find_all("option")
        return len(options)

    def get_product_category_function(self):
        product_category_function = None

        # automatic category detection
        url_id_function_map = {  
            "Hard-disks": self.storage,
            "SSD-Solid-state-drive-": self.storage,
            "Processoren": self.cpu,
            "Videokaarten": self.gpu
        }
        for url_id, function in url_id_function_map.items():
            if url_id in self.url:
                product_category_function = function
                print(f"category ({product_category_function.__name__}) detected in URL".upper())
                break

        # manual category selection
        if not product_category_function:
            selection_function_map = {
                "1": self.storage,
                "2": self.gpu,
                "3": self.cpu,
            }
            for selection, function in selection_function_map.items():
                print(f"{selection}: {function.__name__}")
            product_category_function = selection_function_map.get(
                input("category selection: "))

        return product_category_function

    def extract_products_divs(self) -> list:
        product_divs = []
        for page_number in range(1, self.total_pages + 1):
            page_url = re.sub(r"_p-\d+", f"_p-{page_number}", self.url)
            page_soup = self.get_soup(page_url)
            page_product_divs = page_soup.find_all(
                "div", itemtype="http://schema.org/Product")
            product_divs.extend(page_product_divs)
        return product_divs
    
    def extract_products_data(self, product_divs: list, wanted_data: dict) -> list[dict]:
        """
        TODO extract from product info summary
        TODO for storage : search for capacity in both title and info summary
        """
        products_data = []
        for product_div in product_divs:
            product_data = {}
            for alias, itemprop in wanted_data.items():
                product_data[alias] = product_div.find("meta", {"itemprop": itemprop})["content"]
            products_data.append(product_data)
        return products_data

    def storage():
        pass

    def cpu():
        pass

    def gpu():
        pass
