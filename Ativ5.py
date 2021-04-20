import csv
import math
from igraph import *
from collections import deque

ids = []

class Resultados:
    def __init__(self,raiz,distancias,arvore):
        self.raiz = raiz
        self.distancias = distancias
        self.ag = arvore

    def getRaiz(self):
        return self.raiz

    def getDistancias(self):
        return self.distancias

    def menorDistancia(self,v):
        return self.distancias[v]

    def maiorDistancia(self):
        return max(self.distancias)

    def getArvoreGeradora(self):
        return self.ag

def lerCSV(caminho):
    matriz = []
    with open(caminho) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader.__next__()
        for row in csv_reader:
            matriz = matriz + [row[1:]]
   
    matriz = [[int(j) for j in i] for i in matriz]
    return matriz

def plotarGrafo(matriz, nome):
    g = Graph()
    g.add_vertices(len(matriz))
    
    for v1 in range(len(matriz)-1):
        for v2 in range(v1+1, len(matriz[v1])):
           if(matriz[v1][v2] == 1):
               g.add_edges([(v1,v2)])
    visual_style = {}
    visual_style["vertex_label"] = [str(x) for x in list(range(0, len(matriz)))]
    plot(g, **visual_style, target= nome + ".png")

def BFS(matriz, s):
    ag = []
    for i in matriz:
        ag.append([0]*len(matriz))
    color = ["w"]*len(matriz)
    d = [math.inf]*len(matriz) #distância entre os vértices
    p = [None]*len(matriz) #vértices pai
    q = deque()
    ids = ["r", "s", "t", "u", "v", "w", "x", "y"]
    color[s] = "b"
    d[s] = 0
    q.append(s)
   
    while q:
        for u in q:
            print(ids[u], end=" ")
        print()
        v = q.popleft()
        for j in range(len(matriz[v])):
            if(matriz[v][j] == 1):
                    if (color[j] == "w"):
                        color[j] = "g"
                        q.append(j)
                        ag[v][j] = 1
                        ag[j][v] = 1
                        d[j] = d[v] + 1
                        p[j] = v
        color[j] == "b"
    return Resultados(s,d,ag)

def diametro(distancias):
    maior = max(max(distancias))
    print("Diametro do Grafo:",maior)
    print()

    return maior

def distancias(matriz):
    d = []
    for v in range(len(matriz)):
        d = d + [BFS(matriz, v).getDistancias()]
    print("Distancias:",d)
    print()

    return d

def mediaDistancias(distancias):
    soma = 0
    cont = 0
    for v in range(len(distancias)-1):
        for j in range(v+1, len(distancias)):
            soma = soma + distancias[v][j]
            cont = cont + 1

    print("Distancia media:", soma/cont)
    return soma/cont


""" 
0 => r
1 => s
2 => t
3 => u
4 => v
5 => w
6 => x
7 => y
"""


matriz = lerCSV("Ativ5.csv")
d = distancias(matriz)
mediaDistancias(d)
diametro(d)

print("raiz: s ---------------------------------------------------")
bfs = BFS(matriz, 1)
print(matriz)
print(bfs.getArvoreGeradora())
plotarGrafo(bfs.getArvoreGeradora(),"ArvoreGeradora")
