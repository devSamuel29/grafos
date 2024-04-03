import random
from graphs import *

def get_degree(graph) -> dict:
    n = len(set(v for e in graph for v in e))

    degree_count = {v: sum(1 for edge in graph if v in edge) for v in range(n)}

    return degree_count

def euler(graph: tuple):
    graph_degrees = get_degree(graph)
    count_vertex_degree_odd = sum(1 for degree in graph_degrees.values() if degree % 2 != 0)

    if count_vertex_degree_odd == 0:
        return True, 'O grafo é Euleriano!'
    elif count_vertex_degree_odd == 2:
        return True, 'O grafo é Semi-Euleriano!'

    return False, 'Não é Euleriano!'

def get_weights(graph: tuple):
    n = len(graph)
    weights = [random.randint(0, 10) for _ in range(n)]
    return weights

def get_path(graph: tuple):
    isEulerian, euler_type = euler(graph)

    if(not isEulerian):
        return f'{euler_type}\nNão é possível montar o Caminho Euleriano'

    weights = get_weights(graph)
    graph_degrees = get_degree(graph)

    return f'{euler_type}\nretornar o caminho'

print('GRAFO 1')
print(get_path(graph1))
print()

print('GRAFO 2')
print(get_path(graph2))
print()

print('GRAFO 3')
print(get_path(graph3))
print()

print('GRAFO 4')
print(get_path(graph4))