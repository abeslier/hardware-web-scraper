from websites.passmark import PassMark


def test_get_cpu_scores():
    test_cases = [
        ("AMD Ryzen 5 5600", {"singlethread": 21565, "multithread": 3258}),
        ("Intel Core i7-12700F", {"singlethread": 30556, "multithread": 3862}),
        ("Intel Core i9-13900F", {"singlethread": 50506, "multithread": 4411}),
    ]
    passmark = PassMark()
    for cpu_name, expected_scores in test_cases:
        scores = passmark.get_cpu_scores(cpu_name)
        assert abs(scores["singlethread"] - expected_scores["singlethread"]) <= expected_scores["singlethread"] * 0.01
        assert abs(scores["multithread"] - expected_scores["multithread"]) <= expected_scores["multithread"] * 0.01

def test_get_gpu_score():
    test_cases = [  # 2025-02-24 scores
        ("Quadro K600", 729),
        ("GeForce GT 1030", 2451),
        ("GeForce RTX 3060 12GB", 16896),
        ("GeForce RTX 3060 Ti", 20418),
        ("GeForce RTX 4070", 26969),
        ("Radeon RX 6600", 15124),
    ]
    passmark = PassMark()
    for gpu_name, expected_score in test_cases:
        score = passmark.get_gpu_score(gpu_name)
        assert abs(score - expected_score) <= expected_score * 0.01
