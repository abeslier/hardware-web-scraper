from website import Website


class PassMark(Website):
    CPU_LIST_URL = "https://www.cpubenchmark.net/cpu_list.php"
    GPU_LIST_URL = "https://www.videocardbenchmark.net/gpu_list.php"

    def get_cpu_scores(cpu_name: str) -> dict[str, int]:
        return {"singlethread": 1000, "multithread": 2000}

    def get_gpu_score(gpu_name: str) -> int:
        return 1000
