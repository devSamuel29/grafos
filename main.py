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

    if not isEulerian:
        return f'{euler_type}\nNão é possível montar o Caminho Euleriano'

    weights = get_weights(graph)
    graph_degrees = get_degree(graph)
    start_vertex = next(iter(graph_degrees))
    path = [start_vertex]
    total_weight = 0  # Inicializa o peso total como 0
    weight_sequence = []  # Inicializa a sequência de pesos

    while len(graph) > 0:
        current_vertex = path[-1]
        possible_edges = [edge for edge in graph if current_vertex in edge]

        if len(possible_edges) == 0:
            break

        if len(possible_edges) == 1:
            edge = possible_edges[0]
        else:
            edge_weights = [weights[graph.index(e)] for e in possible_edges]
            min_weight = min(edge_weights)
            min_weight_index = edge_weights.index(min_weight)
            edge = possible_edges[min_weight_index]

        if edge[0] == current_vertex:
            next_vertex = edge[1]
        else:
            next_vertex = edge[0]

        weight = weights[graph.index(edge)]
        total_weight += weight  # Adiciona o peso da aresta ao total
        weight_sequence.append((edge, weight))  # Adiciona a aresta e seu peso à sequência
        path.append(next_vertex)
        graph.remove(edge)

    # Monta a string do caminho com setas "->"
    path_str = " -> ".join(map(str, path))
    # Monta a string da sequência de cálculo dos pesos
    weight_sequence_str = "\n".join([f"Aresta: {edge}, Peso: {weight}" for edge, weight in weight_sequence])
    return f'{euler_type}\nCaminho Euleriano: {path_str}\nPeso Total: {total_weight}\nSequência de Cálculo:\n{weight_sequence_str}'





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
