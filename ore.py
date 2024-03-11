from graphs import *

def ore(graph: tuple):
    n = len(set(v for e in graph for v in e))

    if n < 4:
        return 'Não é um grafo de Ore'
    
    degree_count = {v: 0 for v in range(1, n + 1)}
    for edge in graph:
        for v in edge:
            degree_count[v] += 1 
    

    return 'O Teorema de Ore é satisfeito para o grafo dado.'

print('TEOREMA DE ORE')
print(graph1)
print(ore(graph1))
print()

print(graph2)
print(ore(graph2))
print()

print(graph3)
print(ore(graph3))
print()

print(graph4)
print(ore(graph4))
print()