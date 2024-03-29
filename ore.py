from graphs import *

def ore(graph: list):
    n = len(set(v for e in graph for v in e))
    
    degree_count = {v: 0 for v in range(0, n)}
    for edge in graph:
        for v in edge:
            degree_count[v] += 1
    
    for i in range(0, n):
        for j in range(i, n):
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