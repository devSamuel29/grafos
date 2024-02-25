def create_matrix_adj(dictionary):
    states = list(dictionary.keys())
    num_states = len(states)
    matrix_adj = {state: [0] * num_states for state in states}

    for state in states:
        borders = dictionary[state]
        for border in borders:
            j = states.index(border)
            matrix_adj[state][j] = 1
            
    return matrix_adj

def get_max_degree(dictionary):
    max_degree = 0
    states = []

    for state, degrees in dictionary.items():
        total: int = sum(degrees)
        if total > max_degree:
            max_degree = total
            states = [{"state": state, "borders": [list(dictionary.keys())[i] for i, v in enumerate(dictionary[state]) if v == 1]}]
        elif total == max_degree:
            states.append({"state": state, "borders": [list(dictionary.keys())[i] for i, v in enumerate(dictionary[state]) if v == 1]})

    return {"states": states, "degree": max_degree}

def get_min_degree(dictionary):
    min_degree: int = float('inf')
    states = []

    for state, degrees in dictionary.items():
        total: int = sum(degrees)
        if total < min_degree:
            min_degree = total
            states = [{"state": state, "borders": [list(dictionary.keys())[i] for i, v in enumerate(dictionary[state]) if v == 1]}]
        elif total == min_degree:
            states.append({"state": state, "borders": [list(dictionary.keys())[i] for i, v in enumerate(dictionary[state]) if v == 1]})

    return {"states": states, "degree": min_degree}

def print_result(borders) -> None:
    for state, connections in borders.items():
        print(f'{state}: {connections}')
