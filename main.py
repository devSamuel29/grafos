from graphs import *

def get_degree(graph) -> dict:
    n = len(set(v for e in graph for v in e))

    degree_count = {v: sum(1 for edge in graph if v in edge) for v in range(n)}

    return degree_count

def euler(graph: tuple):
    graph_degrees = get_degree(graph)
    count_vertex_degree_odd = sum(1 for degree in graph_degrees.values() if degree % 2 != 0)

    if count_vertex_degree_odd == 0:
        return 'O grafo é Euleriano!'
    elif count_vertex_degree_odd == 2:
        return 'O grafo é Semi-Euleriano!'

    return 'Não é Euleriano!'

print('GRAFO 1')
print(euler(graph1))
print()

print('GRAFO 2')
print(euler(graph2))
print()

print('GRAFO 3')
print(euler(graph3))
print()

print('GRAFO 4')
print(euler(graph4))