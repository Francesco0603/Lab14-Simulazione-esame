import copy

from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.geni = DAO.getGeni()
        self.grafo = nx.DiGraph()
        self.cromoMap = {}
        self.cromosomi = []
        self.archi = []
        self.Max = 0
        self.Min = 0
        self.sopra = []
        self.sotto = []
    def creaGrafo(self):
        for g in self.geni:
            self.cromoMap[g.__hash__()] = g.Chromosome
            if g.Chromosome not in self.cromosomi and g.Chromosome!=0:
                self.cromosomi.append(g.Chromosome)
                self.grafo.add_node(g.Chromosome)
                print(g.Chromosome)
        for g1 in self.grafo.nodes:
            for g2 in self.grafo.nodes:
                if g1!=g2:
                    p = DAO.getInterazioni(g1,g2)[0]
                    if p != None:
                        self.grafo.add_edge(g1,g2,weight=p)
                        if self.Max < p:
                            self.Max = p
                        if self.Min > p:
                            self.Min = p
    def sottoOsopra(self,s):
        uguale = []
        for e in self.grafo.edges(data=True):
            if e[2]["weight"] <s:
                self.sotto.append(e)
            elif e[2]["weight"] == s:
                uguale.append(e)
            else:
                self.sopra.append(e)

        return len(self.sotto),len(self.sopra),

    def cercaPercorso(self):
        self.bestPercorso = []
        self.pesoMax = 0
        self.ricorsione([],0)
        return self.pesoMax, self.bestPercorso
    def ricorsione(self,parziale,peso):
        if self.pesoMax < peso:
            self.bestPercorso = copy.deepcopy(parziale)
            self.pesoMax = peso
            print(parziale)
            print(peso)
        if len(parziale) == 0:
            for arco in self.sopra:
                parziale.append(arco)
                peso += arco[2]["weight"]
                self.ricorsione(parziale,peso)
                parziale.pop()
                peso -= arco[2]["weight"]
        else:
            for arco in self.sopra:
                if parziale[-1][1] != arco[0] or arco in parziale:
                    continue
                parziale.append(arco)
                peso += arco[2]["weight"]
                self.ricorsione(parziale, peso)
                parziale.pop()
                peso -= arco[2]["weight"]

