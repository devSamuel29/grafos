from collections import defaultdict
import matplotlib.pyplot as plt

def create_matrix_adj(states, edges):
    num_states = len(states)
    matrix_adj = [[0] * num_states for _ in range(num_states)]

    for edge in edges:
        i, j = edge
        matrix_adj[i][j] = 1
        matrix_adj[j][i] = 1 
        
    return matrix_adj

def create_matrix_icd(states, edges):
    num_states = len(states)
    num_edges = len(edges)
    matrix_icd = [[0] * num_edges for _ in range(num_states)]

    for edge in enumerate(edges):
        i, j = edge
        for k in range(0, len(j) - 1):
            matrix_icd[j[k]][i] = 1
            matrix_icd[j[k+1]][i] = 1

    return matrix_icd

def calculate_max_degree_adj(states, matrix):
    max_degree = max(sum(row) for row in matrix)
    borders = {}

    for i, state in enumerate(states):
        degree = sum(matrix[i])
        if degree == max_degree:
            borders[state] = [states[j] for j, val in enumerate(matrix[i]) if val]

    result = []

    result.append('MAX DEGREE STATES')
    for state in borders:
        result.append({
            'state': state,
            'borders': borders[state],
        })
    result.append(f'degree: {max_degree}')

    return result


def calculate_min_degree_adj(states, matrix):
    min_degree = min(sum(row) for row in matrix)
    borders = {}

    for i, state in enumerate(states):
        degree = sum(matrix[i])
        if degree == min_degree:
            borders[state] = [states[j] for j, val in enumerate(matrix[i]) if val]

    result = []

    result.append('MAX DEGREE STATES')
    for state in borders:
        result.append({
            'state': state,
            'borders': borders[state],
        })
    result.append(f'degree: {min_degree}')

    return result

def print_matrix_adj(states, matrix):
    max_state_length = max(len(state) for state in states)
    header = '   ' + ' '.join(state.rjust(max_state_length) for state in states)
    print(header)

    for i, state in enumerate(states):
        row = state.rjust(max_state_length) + ' '
        for j in range(len(states)):
            row += str(matrix[i][j]) + '  '
        print(row)


def print_matrix_icd(vertices, matrix):
    max_vertex_length = max(len(str(vertex)) for vertex in vertices)  
    max_edge_length = len(str(len(matrix[0]))) + 1  
    header = ' ' * max_vertex_length + ' ' + ' '.join(f'e{i}'.rjust(max_edge_length) for i in range(1, len(matrix[0]) + 1))
    print(header)

    for i, vertex in enumerate(vertices):
        row = vertex.rjust(max_vertex_length) 
        for j in range(len(matrix[0])):
            row += str(matrix[i][j]).rjust(max_edge_length) + ' '
        print(row)

def show_hist(states, edges):
    neighbors = defaultdict(set)
    for edge in edges:
        neighbors[states[edge[0]]].add(states[edge[1]])
        neighbors[states[edge[1]]].add(states[edge[0]])

    for state in states:
        if state not in neighbors:
            neighbors[state] = set()

    num_neighbors = [len(neighbors[state]) for state in states]
        
    plt.hist(num_neighbors, bins=range(min(num_neighbors), max(num_neighbors)+2), align='left', edgecolor='black')
    plt.xticks(range(min(num_neighbors), max(num_neighbors)+1))  # Define os ticks no eixo x
    plt.title('Estados x Fronteiras')
    plt.xlabel('Fronteiras')
    plt.ylabel('Estados')
    plt.grid(True)
    plt.show()


def create_indexed_list(states, edges):
    matrix_adj = create_matrix_adj(states, edges)

    indexed_list = [[] for _ in range(len(states))]

    for i in range(len(states)):
        for j in range(len(states)):
            if matrix_adj[i][j] == 1:
                indexed_list[i].append(j)

    return indexed_list


def print_indexed_list(states, indexed_list):
    for i, adjacent_states in enumerate(indexed_list):
        # Imprime o estado e seus estados vizinhos
        print(f"{states[i]}: ", end="")
        for adj in adjacent_states:
            print(states[adj], end=", ")
        print()  
