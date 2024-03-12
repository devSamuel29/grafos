from graphs import *

def dirac(graph: tuple):
    n = len(set(v for e in graph for v in e))

    if n < 3:
        return 'O Teorema de Dirac não é satisfeito para o grafo dado.'
    
    degree_count = {v: 0 for v in range(1, n + 1)}
    for edge in graph:
        for v in edge:
            degree_count[v] += 1 
    
    min_degree = min(degree_count.values())
    
    if min_degree < n / 2: 
        return 'O Teorema de Dirac não é satisfeito para o grafo dado.'

    return 'O grafo satisfaz o Teorema de Dirac'

print('TEOREMA DE DIRAC')
print(graph1)
print(dirac(graph1))
print()

print(graph2)
print(dirac(graph2))
print()

print(graph3)
print(dirac(graph3))
print()

print(graph4)
print(dirac(graph4))
print()
