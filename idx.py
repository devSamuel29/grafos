import json
from fuctions import create_matrix_idx, calculate_max_degree_idx, calculate_min_degree_idx, print_matrix_idx, show_hist_idx

states = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 
          'PB', 'PE', 'PI','PR', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

edges = [
    (0, 2), (0, 21), (1, 15), (1, 4), (1, 25), (2, 22), (2, 21), (2, 13), (2, 10), (3, 13),  
    (4, 7), (4, 8), (4, 9), (4, 12), (4, 15), (4, 16), (4, 25), (4, 26), (5, 16), (5, 19),  
    (5, 14), (5, 15), (6, 8), (6, 12), (7, 12), (7, 18), (8, 10), (8, 11), (8, 12), (8, 26),  
    (9, 13), (9, 16), (9, 26), (10, 11), (10, 13), (10, 21), (10, 26), (11, 12), (11, 17),  
    (11, 24), (12, 18), (12, 24), (13, 26), (13, 22), (14, 19), (14, 15), (15, 16), (16, 26),  
    (17, 23), (17, 24), (18, 24), (20, 23),
]


indexed_list = create_matrix_idx(states, edges)
print_matrix_idx(indexed_list)
print()

max_degree_idx = calculate_max_degree_idx(indexed_list)
print(max_degree_idx)
print()

min_degree_idx = calculate_min_degree_idx(indexed_list)
print(min_degree_idx)
print()

show_hist_idx(indexed_list)
