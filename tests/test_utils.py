from utils import *

def test_is_valid():
    test_cases_megekko = [
        ("https://www.megekko.nl/home/", False),
        ("https://www.megekko.nl/Computer/Componenten/Hard-disks?l=1923", False),
        ("https://www.megekko.nl/Computer/Componenten/Hard-disks/Hard-disks-3-5-?f=f_vrrd-3_s-populair_pp-50_p-1_d-list_cf-", True),
        ("https://www.megekko.nl/Computer/Componenten/Hard-disks/Hard-disks-3-5-?f=f_vrrd-3_s-populair_pp-50_p-1_d-block_cf-", True),
        ("https://www.megekko.nl/Computer/Componenten/Hard-disks/Hard-disks-3-5-?f=f_vrrd-3_s-populair_pp-100_p-2_d-block_cf-", True),
        ("https://www.megekko.nl/product/2036/994018/Hard-disks-3-5-/Seagate-HDD-NAS-3-5-4TB-ST4000VN006-Ironwolf", False),
        ("https://www.megekkoanl/Computer/Componenten/Hard-disks/Hard-disks-3-5-?f=f_vrrd-3_s-populair_pp-100_p-2_d-block_cf-", False),
        ("_d-block_cf-Hard-disks/Hard-disks-3-5-?f=f_vrrd-3_s-populair_pp-100_p-2https://www.megekko.nl/Computer/Componenten/", False),
    ]
    pattern_megekko = r"^(https://www\.megekko\.nl/Computer/Componenten/).*(_d-list_cf-|_d-block_cf-)$"
    for url_megekko, expected in test_cases_megekko:
        assert is_valid(url_megekko, pattern_megekko) == expected
