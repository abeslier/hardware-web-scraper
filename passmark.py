from website import Website


class PassMark(Website):
    VALID_URL_RE = r"^(https://www.cpubenchmark.net|https://www.videocardbenchmark.net)"
    CPU_LIST_URL = "https://www.cpubenchmark.net/cpu_list.php"
    GPU_LIST_URL = "https://www.videocardbenchmark.net/gpu_list.php"
