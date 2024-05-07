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
        ## u -> vertice atual; v -> pai do vertice atual
        u, v = stack.pop()
        if u not in visited:
            visited.add(u)

            ##verifica se nao eh o primeiro da stack
            if v is not None:
                tree.append((v, u))

            for edge in graph:
                ##verifica se a aresta tem U como vertice
                if u in edge:
                    ## caso o edge[1] seja igual ao vertice atual (u), entao o vertice edge[0] eh vizinho do que estamos procurando
                    neighbor = edge[0] if edge[1] == u else edge[1]
                    if neighbor not in visited:
                        stack.append((neighbor, u))

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

print(dfs_recursive_result)
print(dfs_iterative_result)

plot(dfs_recursive_result, dfs_iterative_result)
