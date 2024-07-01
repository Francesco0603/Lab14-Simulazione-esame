from dataclasses import dataclass
@dataclass
class Gene:
    GeneID: str
    Function: str
    Essential: str
    Chromosome: int
    def __hash__(self):
        return self.GeneID,self.Function
