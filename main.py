import json
from fuctions import create_matrix_adj, get_min_degree, get_max_degree, print_result

borders = {
    'AC': ['AM', 'RO'],
    'AL': ['BA', 'SE', 'PE'],
    'AP': ['PA'],
    'AM': ['AC', 'RO', 'RR', 'MT', 'PA'],
    'BA': ['AL', 'SE', 'PE', 'PI', 'TO', 'GO', 'MG', 'ES'],
    'CE': ['PI', 'PB', 'PE'],
    'DF': ['GO', 'MG'],
    'ES': ['BA', 'MG', 'RJ'],
    'GO': ['BA', 'TO', 'DF', 'MG', 'MS'],
    'MA': ['PI', 'TO', 'PA'],
    'MT': ['AM', 'RO', 'PA', 'TO', 'GO', 'MS'],
    'MS': ['MT', 'GO', 'MG', 'SP', 'PR'],
    'MG': ['BA', 'ES', 'RJ', 'SP', 'MS', 'GO', 'DF'],
    'PA': ['AP', 'AM', 'MT', 'TO', 'MA'],
    'PB': ['CE', 'PE'],
    'PR': ['MS', 'SP', 'SC'],
    'PE': ['AL', 'PB', 'CE', 'PI'],
    'PI': ['MA', 'CE', 'PE', 'BA', 'TO'],
    'RJ': ['ES', 'MG', 'SP'],
    'RN': ['PB', 'CE'],
    'RS': ['SC'],
    'RO': ['AM', 'AC', 'MT'],
    'RR': ['AM'],
    'SC': ['RS', 'PR'],
    'SP': ['RJ', 'MG', 'MS', 'PR'],
    'SE': ['AL', 'BA'],
    'TO': ['MA', 'PI', 'BA', 'GO', 'MT', 'PA']
}        

matrix_adj = create_matrix_adj(borders)
print_result(matrix_adj)
print()

max_degree = get_max_degree(matrix_adj)
print("MAX DEGREE:")
print(json.dumps(max_degree, indent=4))
print()

print("MIN DEGREE:")
min_degree = get_min_degree(matrix_adj)
print(json.dumps(min_degree, indent=4))
print()