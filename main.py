from json import loads, dumps
 
with open('response.json') as json_file:
    data = loads(json_file.read())

def dijkstra(graph, start_vertex):
    vertexes = sorted(list(graph.keys()))
    size = len(vertexes)
    start_index = vertexes.index(start_vertex)
    distances = [float('inf')] * size
    distances[start_index] = 0
    visited = [False] * size
    paths = {vertex: [] for vertex in vertexes}
 
    for _ in range(size):
        min_distance = float('inf')
        u = None
        for i in range(size):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                u = i

        if u is None:
            break

        visited[u] = True

        for neighbor, weight in graph[vertexes[u]].items():
            v = vertexes.index(neighbor)
            if not visited[v]:
                alt = distances[u] + weight
                if alt < distances[v]:
                    distances[v] = alt
                    paths[neighbor] = paths[vertexes[u]] + [neighbor]

    result = {}
    for vertex, distance in zip(vertexes, distances):
        if distance == float('inf'):
            result[vertex] = {'distance': 'Infinity', 'path': 'Nao existe um caminho possivel!'}
        else:
            path = [start_vertex] + paths[vertex] if vertex != start_vertex else []
            path_str = ' -> '.join(path)
            result[vertex] = {'distance': distance, 'path': path_str}

    return result

initalVertex = 'A'
print(f'Vertice inicial: {initalVertex}')
print(dumps(dijkstra(data, initalVertex), indent=4))
