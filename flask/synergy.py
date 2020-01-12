#synergy model that stores all synergies

class Synergy:
    def __init__(self, synergyID: int, name: str, desc: str ):
        self.synergyID = synergyID
        self.name = name
        self.desc = desc