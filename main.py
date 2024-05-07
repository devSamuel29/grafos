from json import load
import networkx as nx
import matplotlib.pyplot as plt

def dfs_recursive(graph: list, vertex: int, visited: set = None) -> list: 
    if visited is None:
        visited = set()

    visited.add(vertex)
    tree = []
    for edge in graph:
        if vertex in edge:
            neighbor = edge[0] if edge[1] == vertex else edge[1]
            if neighbor not in visited:
                tree.append((vertex, neighbor))
                tree.extend(dfs_recursive(graph, neighbor, visited))

    return tree

def dfs_iterative(graph: list, initial_vertex: int) -> list:
    visited = set()

    ## armazenando vertice que irao ser explorados
    stack = [(initial_vertex, None)]

    ## armazena as arestas da arvore
    tree = []

    ##enquanto houver vertices na pilha
    while stack:
        ## child -> vertice atual; parent -> pai do vertice atual
        child, parent = stack.pop()
        if child not in visited:
            visited.add(child)

            ##verifica se nao eh o primeiro da stack
            if parent is not None:
                tree.append((parent, child))

            for edge in graph:
                ##verifica se a aresta tem U como vertice
                if child in edge:
                    ## caso o edge[1] seja igual ao vertice atual (child), entao o vertice edge[0] eh vizinho do que estamos procurando
                    neighbor = edge[0] if edge[1] == child else edge[1]
                    if neighbor not in visited:
                        stack.append((neighbor, child))

    return tree

def plot(dfs_recursive: list, dfs_interative: list) -> None:
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    T_recursive = nx.Graph(dfs_recursive)
    nx.draw(T_recursive, with_labels=True, node_color='skyblue', font_size=12, font_weight='bold')
    plt.title("Árvore DFS Recursiva")

    plt.subplot(1, 2, 2)
    T_iterative = nx.Graph(dfs_interative)
    nx.draw(T_iterative, with_labels=True, node_color='lightgreen', font_size=12, font_weight='bold')
    plt.title("Árvore DFS Iterativa")
    
    plt.tight_layout()
    plt.show()

with open('response.json') as f:
    data = load(f)

edges = data['edges']
inital_vertex = data['initialVertex']

dfs_recursive_result = dfs_recursive(edges, inital_vertex)
dfs_iterative_result = dfs_iterative(edges, inital_vertex)

plot(dfs_recursive_result, dfs_iterative_result)
