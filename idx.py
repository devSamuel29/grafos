import json
from fuctions import create_matrix_idx, calculate_max_degree_idx, calculate_min_degree_idx, print_matrix_idx, show_hist_idx

states = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 
          'PB', 'PE', 'PI','PR', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

edges =  [
    (0, 2), (0, 21),
    (1, 4), (1, 15), (1, 25),
    (2, 0), (2, 10), (2, 13), (2, 21), (2, 22),
    (3, 13),
    (4, 1), (4, 7), (4, 8), (4, 9), (4, 12), (4, 15), (4, 16), (4, 25), (4, 26),
    (5, 14), (5, 15), (5, 16), (5, 19),
    (6, 8), (6, 12),
    (7, 4), (7, 12), (7, 18),
    (8, 4), (8, 6), (8, 10), (8, 11), (8, 12), (8, 26),
    (9, 4), (9, 13), (9, 16), (9, 26),
    (10, 2), (10, 8), (10, 11), (10, 13), (10, 21), (10, 26),
    (11, 8), (11, 10), (11, 12), (11, 17), (11, 24),
    (12, 4), (12, 6), (12, 7), (12, 8), (12, 11), (12, 18), (12, 24),
    (13, 2), (13, 3), (13, 9), (13, 10), (13, 22), (13, 26),
    (14, 5), (14, 15), (14, 19),
    (15, 1), (15, 4), (15, 5), (15, 14), (15, 16),
    (16, 4), (16, 5), (16, 9), (16, 15), (16, 26),
    (17, 11), (17, 23), (17, 24),
    (18, 7), (18, 12), (18, 24),
    (19, 5), (19, 14),
    (20, 23),
    (21, 0), (21, 2), (21, 10),
    (22, 2), (22, 13),
    (23, 17), (23, 20),
    (24, 11), (24, 12), (24, 17), (24, 18),
    (25, 1), (25, 4),
    (26, 4), (26, 8), (26, 9), (26, 10), (26, 13), (26, 16)
]

def create_list_idx(states, edges):
    connections = {}
    beta = []
    alpha = [0] 

    for edge in edges:
        beta.append(states[edge[1]])

    for i in range(1, len(edges)):
        if edges[i][0] != edges[i - 1][0]:
            alpha.append(i)
    alpha.append(len(edges)) 

    for i in range(len(alpha) - 1):
        state = states[edges[alpha[i]][0]]
        connected_states = beta[alpha[i]:alpha[i + 1]]
        connections[state] = sorted(list(set(connected_states)))

    return connections                  
        
      

print(create_list_idx(states, edges))