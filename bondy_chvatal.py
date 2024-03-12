from graphs import *

def bondy_chvatal(graph: tuple):
    n = len(set(v for e in graph for v in e))

    if n < 3:
        return 'O Teorema de Bondy e Chvátal não é satisfeito para o grafo dado.'
    
    for i in range(len(graph)):
        for j in range(i+1, len(graph)):
            u, v = graph[i]
            x, y = graph[j]
            if u != x and u != y and v != x and v != y:
                degree_sum = sum((u == edge[0] or u == edge[1]) + (v == edge[0] or v == edge[1]) for edge in graph)
                if degree_sum < n:
                    return 'O Teorema de Bondy e Chvátal não é satisfeito para o grafo dado.'
    
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