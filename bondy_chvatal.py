from graphs import *

def bondy_chvatal(graph: list):
    n = len(set(v for e in graph for v in e))

    if n < 3:
        return 'O Teorema de Bondy e Chvátal não é satisfeito para o grafo dado.'
        
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) not in graph and (j, i) not in graph:
                graph.append((i, j))

    return 'O grafo satisfaz o Teorema de Bondy e Chvátal'

print('TEOREMA DE BONDY E CHVATAL')
print(graph1)
print(bondy_chvatal(graph1))
print()

print(graph2)
print(bondy_chvatal(graph2))
print()

print(graph3)
print(bondy_chvatal(graph3))
print()

print(graph4)
print(bondy_chvatal(graph4))
print()