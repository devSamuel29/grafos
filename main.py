from graphs import *

def get_degree(graph) -> dict:
    n = len(set(v for e in graph for v in e))

    degree_count = {v: sum(1 for edge in graph if v in edge) for v in range(n)}

    return degree_count

def euler(graph: tuple) -> bool:
    graph_degrees = get_degree(graph)
    
    if any(degree % 2 != 0 for degree in graph_degrees.values()):
        return False

    return True

def semi_euler(graph: tuple) -> bool:
    graph_degrees = get_degree(graph)

    count_vertex_degree_odd = sum(1 for degree in graph_degrees.values() if degree % 2 != 0)

    if count_vertex_degree_odd != 2:
        return False

    return True

def check_eulerianity(graph: tuple):
    if euler(graph):
        print('O grafo é Euleriano!')
    elif semi_euler(graph):
        print('O grafo é Semi-Euleriano!')
    else:
        print('Não é Euleriano!')

print('GRAFO 1')
check_eulerianity(graph1)
print()

print('GRAFO 2')
check_eulerianity(graph2)
print()

print('GRAFO 3')
check_eulerianity(graph3)
print()

print('GRAFO 4')
check_eulerianity(graph4)