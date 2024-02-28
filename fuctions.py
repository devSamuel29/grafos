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

    return matrix_icd

def calculate_max_degree(states, adjacency_matrix):
    max_degree = max(sum(row) for row in adjacency_matrix)
    borders = {}

    for i, state in enumerate(states):
        degree = sum(adjacency_matrix[i])
        if degree == max_degree:
            borders[state] = [states[j] for j, connected in enumerate(adjacency_matrix[i]) if connected]

    result = []
    for state in borders:
        result.append({
            'state': state,
            'borders': borders[state],
            'degree': max_degree
        })

    return result

def calculate_min_degree(states, matrix):
    min_degree = min(sum(row) for row in matrix)
    borders = {}

    for i, state in enumerate(states):
        degree = sum(matrix[i])
        if degree == min_degree:
            borders[state] = [states[j] for j, connected in enumerate(matrix[i]) if connected]

    result = []
    for state in borders:
        result.append({
            'state': state,
            'borders': borders[state],
            'degree': min_degree
        })

    return result

def print_matrix(states, matrix):
    max_state_length = max(len(state) for state in states)
    header = "   " + " ".join(state.rjust(max_state_length) for state in states)
    print(header)

    for i, state in enumerate(states):
        row = state.rjust(max_state_length) + " "
        for j in range(len(states)):
            row += str(matrix[i][j]) + "  "
        print(row)
