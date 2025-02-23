from websites.megekko import Megekko


class Component():
    def __init__(self):
        self.name = None
        self.code = None
        self.prices = {Megekko: None}


class CPU(Component):
    def __init__(self):
        super().__init__()
        self.singlethread_score = None  # passmark
        self.multithread_score = None  # passmark
        self.cores = None
        self.threads = None
        self.clock = None
        self.boost = None
        self.socket = None
        self.tdp = None
        self.igpu = None
        self.unlocked = None


class GPU(Component):
    def __init__(self):
        super().__init__()
        self.score = None
        self.vram = None


class RAM(Component):
    def __init__(self):
        super().__init__()
        self.type = None  # .../DDR4/DDR5
        self.format = None  # DIMM/SODIMM
        self.capacity = None
        self.speed = None
        self.latency = None
        self.modules = None  # 1/2/4/...


class PSU(Component):
    def __init__(self):
        super().__init__()
        self.wattage = None
        self.efficiency = None
        self.size = None  # ATX/SFX/...
        self.modularity = None  # full/semi/none
        self.tier = None  # https://cultists.network/140/psu-tier-list/


class Storage(Component):
    def __init__(self):
        super().__init__()
        self.capacity = None


class Cooler(Component):
    def __init__(self):
        super().__init__()
        self.sockets = []
        self.height = None
        self.nspr = None  # https://noctua.at/en/noctua-standardised-performance-rating
