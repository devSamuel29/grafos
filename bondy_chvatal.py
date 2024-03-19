from graphs import *

def get_degree(graph):
    n = len(set(v for e in graph for v in e))

    degree_count = {v: 0 for v in range(0, n)}
    for edge in graph:
        for v in edge:
            degree_count[v] += 1

    sorted_degree = sorted(degree_count.items(), key=lambda item: item[1], reverse=True)

    sorted_dict = {vertex: degree for vertex, degree in sorted_degree}

    return sorted_dict

def bondy_chvatal(graph: list):
    n = len(set(v for e in graph for v in e))

    if n < 3:
        return 'O Teorema de Bondy e Chvátal não é satisfeito para o grafo dado.'
    
    degree_count = get_degree(graph)
    non_adj = []

    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) not in graph and (j, i) not in graph:
                non_adj.append((i, j))

    non_adj_sorted = sorted(non_adj, key=lambda pair: degree_count[pair[0]] + degree_count[pair[1]], reverse=True)

    for vertex_pair in non_adj_sorted:
        i, j = vertex_pair
        if degree_count[i] + degree_count[j] >= n:
            graph.append(vertex_pair)
            degree_count = get_degree(graph)

    for i in range(0, n):
        for j in range(i, n):
            if (i, j) not in graph and (j, i) not in graph:
                if degree_count[i] + degree_count[j] < n:
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