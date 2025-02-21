from megekko import Megekko
from utils import *


def main():
    url = input("URL: ")
    megekko = Megekko(url)
    print_csv(export_csv(megekko.extracted_products_data))


if __name__ == "__main__":
    main()
