from megekko import Megekko
from passmark import PassMark
from utils import *


def main():
    megekko = Megekko(input("URL: "))
    print_csv(export_csv(megekko.extracted_products_data))

    passmark = PassMark()


if __name__ == "__main__":
    main()
