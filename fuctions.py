import json
import matplotlib.pyplot as plt

# ADJACENCY #

def create_adjacency_matrix(states, edges):
    num_states = len(states)
    adjacency_matrix = {state: [0] * num_states for state in states}

    for edge in edges:
        i, j = edge
        adjacency_matrix[states[i]][j] = 1
        adjacency_matrix[states[j]][i] = 1 
        
    return adjacency_matrix

def calculate_max_degree_adj(adjacency_matrix):
    max_degree = max(sum(connections) for connections in adjacency_matrix.values())
    max_degree_states = {}

    for state, connections in adjacency_matrix.items():
        degree = sum(connections)
        if degree == max_degree:
            state_index = list(adjacency_matrix.keys()).index(state)
            max_degree_states[state] = [neighbor_state for neighbor_state, val in adjacency_matrix.items() if val[state_index]]

    result = []

    result.append('MAX DEGREE STATES')
    for state, borders in max_degree_states.items():
        result.append({
            'state': state,
            'borders': borders,
        })
    result.append(f'degree: {max_degree}')

    return json.dumps(result, indent=4)


def calculate_min_degree_adj(adjacency_matrix):
    min_degree = min(sum(connections) for connections in adjacency_matrix.values())
    min_degree_states = {}

    for state, connections in adjacency_matrix.items():
        degree = sum(connections)
        if degree == min_degree:
            state_index = list(adjacency_matrix.keys()).index(state)
            min_degree_states[state] = [neighbor_state for neighbor_state, val in adjacency_matrix.items() if val[state_index]]

    result = []

    result.append('MIN DEGREE STATES')
    for state, borders in min_degree_states.items():
        result.append({
            'state': state,
            'borders': borders,
        })
    result.append(f'degree: {min_degree}')

    return json.dumps(result, indent=4)

def print_adjacency_matrix(adjacency_matrix):
    for state, values in adjacency_matrix.items():
        print(f"{state}: {values}")

def show_hist_adj(adjacency_matrix):
    num_neighbors = [sum(connections) for connections in adjacency_matrix.values()]

    plt.hist(num_neighbors, bins=range(min(num_neighbors), max(num_neighbors)+2), align='left', edgecolor='black')
    plt.xticks(range(min(num_neighbors), max(num_neighbors)+1))
    plt.title('Distribuição de Vizinhos dos Estados')
    plt.xlabel('Número de Vizinhos')
    plt.ylabel('Número de Estados')
    plt.grid(True)
    plt.show()

###

# INCIDENCE #
    
def create_incidence_matrix(states, edges):
    incidence_matrix = {state: [0] * len(edges) for state in states}

    for i, (state_index1, state_index2) in enumerate(edges):
        incidence_matrix[states[state_index1]][i] = 1
        incidence_matrix[states[state_index2]][i] = 1

    return incidence_matrix

def calculate_max_degree_icd(incidence_matrix):
    max_degree = 0
    state_degrees = {}

    for state, borders in incidence_matrix.items():
        degree = sum(borders)
        state_degrees[state] = degree
        if degree > max_degree:
            max_degree = degree

    max_degree_states = ['MAX DEGREE STATES']
    for state, degree in state_degrees.items():
        if degree == max_degree:
            border_states = []
            for i, border in enumerate(incidence_matrix[state]):
                if border == 1:
                    for other_state, other_borders in incidence_matrix.items():
                        if other_borders[i] == 1 and other_state != state:
                            border_states.append(other_state)
                            break

            max_degree_states.append({
                'state': state,
                'borders': border_states
            })

    max_degree_states.append(f'degree: {max_degree}')
    return json.dumps(max_degree_states, indent=4)

def calculate_min_degree_icd(incidence_matrix):
    min_degree = float('inf')
    state_degrees = {}

    for state, borders in incidence_matrix.items():
        degree = sum(borders)
        state_degrees[state] = degree
        if degree < min_degree:
            min_degree = degree

    min_degree_states = ['MIN DEGREE STATES']
    for state, degree in state_degrees.items():
        if degree == min_degree:
            border_states = []
            for i, border in enumerate(incidence_matrix[state]):
                if border == 1:
                    for other_state, other_borders in incidence_matrix.items():
                        if other_borders[i] == 1 and other_state != state:
                            border_states.append(other_state)
                            break

            min_degree_states.append({
                'state': state,
                'borders': border_states
            })

    min_degree_states.append(f'degree: {min_degree}')
    return json.dumps(min_degree_states, indent=4)

def print_incidence_matrix(incidence_matrix):
    for state, values in incidence_matrix.items():
        print(f"{state}: {values}")
        
def show_hist_icd(incidence_matrix):
    num_connections = [sum(values) for values in incidence_matrix.values()]

    plt.hist(num_connections, bins=range(min(num_connections), max(num_connections)+2), align='left', edgecolor='black')
    plt.xticks(range(min(num_connections), max(num_connections)+1))
    plt.title('Distribuição de Fronteiras dos Estados')
    plt.xlabel('Número de Fronteiras')
    plt.ylabel('Número de Estados')
    plt.grid(True)
    plt.show()

###

# LISTA INDEXADA #

def create_matrix_idx(states, edges):
    adjacency_matrix = create_adjacency_matrix(states, edges)

    indexed_list = {state: [] for state in states}

    for state, connections in adjacency_matrix.items():
        for neighbor_state, connection in zip(states, connections):
            if connection == 1:
                indexed_list[state].append(neighbor_state)

    return indexed_list

def calculate_max_degree_idx(indexed_list):
    max_degree = max(len(neighbours) for neighbours in indexed_list.values())
    max_degree_states = {state: neighbours for state, neighbours in indexed_list.items() if len(neighbours) == max_degree}

    result = ['MAX DEGREE STATES']
    for state, neighbours in max_degree_states.items():
        result.append({'state': state, 'borders': neighbours})
    result.append(f'degree: {max_degree}')

    return json.dumps(result, indent=4)

def calculate_min_degree_idx(indexed_list):
    min_degree = min(len(neighbours) for neighbours in indexed_list.values())
    min_degree_states = {state: neighbours for state, neighbours in indexed_list.items() if len(neighbours) == min_degree}

    result = ['MIN DEGREE STATES']
    for state, neighbours in min_degree_states.items():
        result.append({'state': state, 'borders': neighbours})
    result.append(f'degree: {min_degree}')

    return json.dumps(result, indent=4)

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

###