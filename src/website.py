from bs4 import BeautifulSoup
import requests, sys

from utils import *


class Website:
    def is_valid_url(self, url: str, pattern) -> bool:
        return is_valid(url, pattern)

    def get_soup(self, url: str) -> BeautifulSoup:
        response = requests.get(url)
        return BeautifulSoup(response.text, "html.parser")
