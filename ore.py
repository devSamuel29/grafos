from graphs import *

def ore(graph: tuple):
    n = len(set(v for e in graph for v in e))

    if n < 3:
        return 'Não é um grafo de Ore'
    
    degree_count = {v: 0 for v in range(1, n + 1)}
    for edge in graph:
        for v in edge:
            degree_count[v] += 1

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if (i, j) not in graph and (j, i) not in graph:
                if degree_count[i] + degree_count[j] < n:
                    return 'O Teorema de Ore não é satisfeito para o grafo dado.'
                
    return 'O grafo satisfaz o Teorema de Ore'
                
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