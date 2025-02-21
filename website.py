from bs4 import BeautifulSoup
import requests, re, sys


class Website:
    def __init__(self, url: str):
        if not self.is_valid_url(url):
            sys.exit("INVALID URL")
        self.url = url

    def is_valid_url(self, url: str) -> bool:
        # `VALID_URL_RE` defined in child class
        return bool(re.match(self.__class__.VALID_URL_RE, url))

    def get_soup(self, url: str) -> BeautifulSoup:
        response = requests.get(url)
        return BeautifulSoup(response.text, "html.parser")
