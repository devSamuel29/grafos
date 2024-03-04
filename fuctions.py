import matplotlib.pyplot as plt

def create_matrix_adj(states, edges):
    num_states = len(states)
    matrix_adj = [[0] * num_states for _ in range(num_states)]

    for edge in edges:
        i, j = edge
        matrix_adj[i][j] = 1
        matrix_adj[j][i] = 1 
        
    return matrix_adj

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

    result.append('MIN DEGREE STATES')
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

def show_hist_adj(matrix_adj):
    num_neighbors = [sum(row) for row in matrix_adj]

    plt.hist(num_neighbors, bins=range(min(num_neighbors), max(num_neighbors)+2), align='left', edgecolor='black')
    plt.xticks(range(min(num_neighbors), max(num_neighbors)+1))
    plt.title('Distribuição de Fronteiras dos Estados')
    plt.xlabel('Número de Fronteiras')
    plt.ylabel('Número de Estados')
    plt.grid(True)
    plt.show()
    
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
        
def show_hist_icd(incidence_matrix):
    num_connections = [sum(row) for row in incidence_matrix]

    plt.hist(num_connections, bins=range(min(num_connections), max(num_connections)+2), align='left', edgecolor='black')
    plt.xticks(range(min(num_connections), max(num_connections)+1))
    plt.title('Distribuição de Fronteiras dos Estados')
    plt.xlabel('Número de Fronteiras')
    plt.ylabel('Número de Estados')
    plt.grid(True)
    plt.show()

def create_matrix_idx(states, edges):
    matrix_adj = create_matrix_adj(states, edges)

    indexed_list = {state: [] for state in states}

    for i in range(len(states)):
        for j in range(len(states)):
            if matrix_adj[i][j] == 1:
                indexed_list[states[i]].append(states[j])

    return indexed_list

def calculate_max_degree_idx(indexed_list):
    max_degree = max(len(neighbours) for neighbours in indexed_list.values())
    max_degree_states = {state: neighbours for state, neighbours in indexed_list.items() if len(neighbours) == max_degree}

    result = ['MAX DEGREE STATES']
    for state, neighbours in max_degree_states.items():
        result.append({'state': state, 'borders': neighbours})
    result.append(f'degree: {max_degree}')

    return result

def calculate_min_degree_idx(indexed_list):
    min_degree = min(len(neighbours) for neighbours in indexed_list.values())
    min_degree_states = {state: neighbours for state, neighbours in indexed_list.items() if len(neighbours) == min_degree}

    result = ['MIN DEGREE STATES']
    for state, neighbours in min_degree_states.items():
        result.append({'state': state, 'borders': neighbours})
    result.append(f'degree: {min_degree}')

    return result

def print_matrix_idx(indexed_list):
    for state, borders in indexed_list.items():
        borders_str = ', '.join(borders)
        print(f'{state}: {borders_str}')

def show_hist_idx(indexed_list):
    num_neighbors = [len(neighbors) for neighbors in indexed_list.values()]

    plt.hist(num_neighbors, bins=range(min(num_neighbors), max(num_neighbors)+2), align='left', edgecolor='black')
    plt.xticks(range(min(num_neighbors), max(num_neighbors)+1))
    plt.title('Distribuição de Fronteiras dos Estados')
    plt.xlabel('Número de Fronteiras')
    plt.ylabel('Número de Estados')
    plt.grid(True)
    plt.show()
