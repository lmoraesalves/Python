# #introdução a listas
#     # Armazenar mais de uma informação em uma variável
#     # Manter a sequência dos dados em uma variável

# var_cidades = [
#     'Rio de Janeiro', 
#     'São Paulo', 
#     'Salvador'
#     ]

# print(var_cidades)

# #Manipulando Listas

# var_cidades = [
#     'Rio de Janeiro', #index 0
#     'São Paulo', #Index 1
#     'Salvador', #Index 2
#     'Goiania' #Index 3
#     ]

# var_cidades[0] = 'Brasilia'
# print(var_cidades[1], var_cidades[2])


# # Funções dentro de listas

# var_cidades = [
#     'Rio de Janeiro', #index 0
#     'São Paulo', #Index 1
#     'Salvador', #Index 2
#     'Goiania' #Index 3
#     ]

# # var_cidades.append('Santa Catarina')
# # var_cidades.remove(var_cidades[0])
# # var_cidades.insert(1, 'Santa Catarina')
# # var_cidades.pop(0)
# # var_cidades.sort()

# print(var_cidades)

# # Concatenando Listas

# var_numeros = [
#     1, #index 0
#     2, #Index 1
#     3, #Index 2
#     4 #Index 3
#     ]

# var_letras = [
#     'a',
#     'b',
#     'c',
#     'd'
# ]

# # var_final = var_numeros + var_letras
# var_numeros.extend(var_letras)

# print(var_numeros)

# Listas dentro de listas

var_itens = [
    ['Item 1', 'Item 2'],
    ['Item 3', 'Item 4']
]

print(var_itens[0][1])