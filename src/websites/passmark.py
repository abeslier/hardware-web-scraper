from website import Website


class PassMark(Website):
    CPU_LIST_URL = "https://www.cpubenchmark.net/cpu_list.php"
    GPU_LIST_URL = "https://www.videocardbenchmark.net/gpu_list.php"
    CPU_LOOKUP_LIST_URL_BASE = "https://www.cpubenchmark.net/cpu_lookup.php?cpu="
    GPU_LOOKUP_LIST_URL_BASE = "https://www.videocardbenchmark.net/video_lookup.php?gpu="
    CPU_PAGE_URL_BASE = "https://www.cpubenchmark.net/cpu.php?cpu="
    GPU_PAGE_URL_BASE = "https://www.videocardbenchmark.net/gpu.php?gpu="

    def find_href_id(self, pu_list_url: str, separator: str, pu_name: str) -> str:
        """
        e.g.
        1. with `Radeon RX 6600`
        2. find `<a href="video_lookup.php?gpu=Radeon+RX+6600&amp;id=4465">Radeon RX 6600</a>`
        3. to extract `Radeon+RX+6600&id=4465`
        4. which will be used to complete the page url where the scores are located
        """
        soup = self.get_soup(pu_list_url)
        a = soup.find_all("a", string=pu_name)
        if len(a) == 1:  # else: not found, or multiple matches found
            pu_lookup_list_url_end = a[0].get("href")
            pu_href_id = pu_lookup_list_url_end.split(separator)[-1]
            return pu_href_id

    def get_cpu_scores(self, cpu_name: str) -> dict[str, int]:
        cpu_href_id = self.find_href_id(self.CPU_LIST_URL, "?cpu=", cpu_name)
        cpu_page_url = self.CPU_PAGE_URL_BASE + cpu_href_id

        soup = self.get_soup(cpu_page_url)
        multithread_title_div = soup.find("div", string="Multithread Rating")
        multithread_score_div = multithread_title_div.find_next("div")
        singlethread_title_div = soup.find("div", string="Single Thread Rating")
        singlethread_score_div = singlethread_title_div.find_next("div")

        multithread_score = int(singlethread_score_div.text)
        singlethread_score = int(multithread_score_div.text)
        return {"singlethread": singlethread_score, "multithread": multithread_score}

    def get_gpu_score(self, gpu_name: str) -> int:
        gpu_href_id = self.find_href_id(self.GPU_LIST_URL, "?gpu=", gpu_name)
        gpu_page_url = self.GPU_PAGE_URL_BASE + gpu_href_id

        soup = self.get_soup(gpu_page_url)
        speedicon_div = soup.find("div", class_="speedicon")
        score_span = speedicon_div.find_next("span")
        
        score = int(score_span.text)
        return score
