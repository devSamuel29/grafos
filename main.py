from json import dumps, load

def bellman_ford(graph, vertexes, initial_vertex):
    # Inicializa o número de vértices e define as distâncias iniciais como infinito
    num_vertexes = len(vertexes)
    distances = {vertex: float('inf') for vertex in vertexes} # Inicializa as distancias como infinito para todos o vertices
    distances[initial_vertex] = 0  # A distância do vértice inicial para ele mesmo é 0
    predecessors = {vertex: None for vertex in vertexes} # Predecessores são inicialmente None

    # Cria uma lista de todas as arestas no grafo, com seus respectivos pesos
    edges = []
    for u in graph:
        for v in graph[u]:
            edges.append((u, v, graph[u][v]))
            print(edges)

    # Relaxa todas as arestas num_vertexes - 1 vezes
    for _ in range(num_vertexes - 1):
        for u, v, weight in edges:
            # Verifica se a distância pode ser reduzida
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u  # Atualiza o predecessor

    # Verifica por ciclos de peso negativo
    for _ in range(num_vertexes - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = float('-inf')
                predecessors[v] = None  # Remove o predecessor

    # Verifica novamente para marcar todos os vértices alcançáveis a partir de ciclos de peso negativo
    for _ in range(num_vertexes - 1):
        for u, v, weight in edges:
            if distances[u] == float('-inf'):
                distances[v] = float('-inf')
                predecessors[v] = None

    # Cria o resultado final, com caminhos e pesos para cada vértice
    result = {}

    for vertex in vertexes:
        if distances[vertex] == float('inf'):
            result[vertex] = {'path': 'There is no possible path!', 'weight': float('inf')}
        elif distances[vertex] == float('-inf'):
            result[vertex] = {'path': 'There is no possible path! (Cyclic)', 'weight': float('-inf')}
        else:
            # Reconstrói o caminho a partir dos predecessores
            path = []
            current_vertex = vertex
            while current_vertex is not None:
                path.insert(0, current_vertex)
                current_vertex = predecessors[current_vertex]
            result[vertex] = {'path': ' -> '.join(path), 'weight': distances[vertex]}
    
    # Ordena o resultado de acordo com os vértices
    sorted_result = {vertex: result[vertex] for vertex in sorted(result.keys())}
    return sorted_result

with open('response.json') as json_file:
    data = load(json_file)
    
vertexes = set(data.keys())
initialVertex = 'S'

distances = bellman_ford(data, vertexes, initialVertex)
print(f'Vertice inicial: {initialVertex}')
print(dumps(distances, indent=4))
