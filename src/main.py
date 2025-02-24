from websites.megekko import Megekko
from websites.passmark import PassMark
from utils import *


def main():
    #megekko = Megekko(input("URL: "))
    #print_csv(export_csv(megekko.extracted_products_data))

    passmark = PassMark()
    print(passmark.get_cpu_scores("AMD Ryzen 5 5600"))
    print(passmark.get_gpu_score("Radeon RX 6600"))


if __name__ == "__main__":
    main()
