from copy import deepcopy
import json
from math import inf
import igraph as ig
from collections import deque

def generate_bfs_tree(graph, initial_vertex):
    state_vertex = {vertex: 'not visited' for vertex in range(len(graph))}
    depth_vertex = [inf] * len(graph)
   
    queue = deque()
    
    initial_vertex = initial_vertex - 1
    queue.append(initial_vertex)
    depth_vertex[initial_vertex] = 0

    bfs_tree = []
    aux_graph = deepcopy(graph)

    while queue:
        current_vertex = queue.popleft()
        neighbors = [i for i, edges in enumerate(aux_graph[current_vertex]) if edges == 1]
        for neighbor in neighbors:
            if state_vertex[neighbor] == 'not visited':
                state_vertex[neighbor] = 'discovered'
                queue.append(neighbor)
                aux_graph[current_vertex][neighbor] = 0
                aux_graph[neighbor][current_vertex] = 0

                depth_vertex[neighbor] = depth_vertex[current_vertex] + 1
                bfs_tree.append((current_vertex, neighbor))
        state_vertex[current_vertex] = 'visited'
    return bfs_tree, depth_vertex

def draw_tree(tree, depth, root):
    g = ig.Graph(directed=True)
    g.add_vertices(len(depth))

    labels = [f'{i+1}\n({depth[i]})' for i in range(len(depth))]
    g.vs["label"] = labels

    g.add_edges(tree)

    layout = g.layout_reingold_tilford(root=[int(root) - 1])

    plot = ig.plot(g, layout=layout, vertex_size=30, vertex_color='lightblue',
                   vertex_label_size=14, vertex_label_color='black', vertex_label_font='Arial',
                   edge_color='brown', edge_arrow_size=1)
    plot.save(f'Root{root}.png')


def shortest_path(tree, root, destination):
    root = root - 1
    destination = destination - 1
    paths = {root: [root]}
    visited = set([root])
    queue = deque([root])

    while queue:
        current_vertex = queue.popleft()
        for parent, child in tree:
            if parent == current_vertex and child not in visited:
                path_to_child = paths[current_vertex] + [child]
                paths[child] = path_to_child
                visited.add(child)
                queue.append(child)
    path = paths.get(destination)
    return ' -> '.join(map(lambda vertex: str(vertex + 1), path)) if path else None

file = json.load(open('response.json'))

num_vertices = file['numEdges']

edges = file['edges']

vertices = [i for i in range(int(num_vertices))]

graph = [[0] * num_vertices for _ in range(num_vertices)]
for edge in edges:
    graph[edge[0] - 1][edge[1] - 1] = 1
    graph[edge[1] - 1][edge[0] - 1] = 1

initialVertex = file['initialVertex']
finalVertex = file['finalVertex']

bfs_tree, depth = generate_bfs_tree(graph, initialVertex)
draw_tree(bfs_tree, depth, initialVertex)

shortest_path = shortest_path(bfs_tree, initialVertex, finalVertex)

if shortest_path:
    print(shortest_path)
else:
    print(f'No path found')
