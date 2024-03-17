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

# # Listas dentro de listas

# var_numero = [1, 2, 3, 4]
# print(var_numero[1])

# var_itens = [
#     ['Item 1', 'Item 2'],
#     ['Item 3', 'Item 4']
# ]

# print(var_itens[0][1])

# # Extrair variáveis de Listas *Unpacking list*
#     # Armazenar mais de uma infromação em variáveis
#     # Manter a sequencia dos dados em uma variavel

# var_produtos = [
#     'Arroz',    #Index0
#     'Feijão',   #Index1
#     'Laranja',  #Index2
#     'Banana'    #Index3
# ]

# var_item1, var_item2, var_item3, *var_outros = var_produtos

# print(var_item1)
# print(var_item2)
# print(var_item3)
# print(var_outros)

# #For loop dentro de uma lista

# var_valores = [10, 20, 40, 80, 160]

# for var_x in var_valores:
#     print(f'O valor final do seu produto é: R${var_x}')

# # Verificando itens em uma lista

# var_cor_client = input('Digite a cor da tinta: ')
# # var_cor_client = var_cor_client.lower()

# var_cor = [
#     'amarelo',
#     'verde',
#     'azul',
#     'vermelho'
#     ]

# if var_cor_client.lower() in var_cor:
#     print(f'A cor {var_cor_client.lower()} está disponível.')
# else:
#     print(f'A cor {var_cor_client.lower()} não está disponível.')

# # Agregando duas listas com o ZIP

# var_cor = [
#     'amarelo',
#     'verde',
#     'azul',
#     'vermelho'
#     ]

# var_valor = [
#     10, 20, 30, 40
#     ]

# var_consolidado = zip(var_cor, var_valor)

# print(list(var_consolidado))

# # Criar uma lista de frutas a partir do input fornecido pelo User

# var_frutas_user = input('Por gentileza, digite as frutas que deseja comprar, separados por vírgula: ')
# var_frutas_list = var_frutas_user.split(', ')


# print(var_frutas_list)


# #tuples
#     # Armazenar mais de uma informação em variaveis
#     # Manter a sequencia dos dados em uma variavel
#     # Não pode ser alteradar (immutable)

# var_cores_list = ['amarelo', 'verde', 'azul', 'vermelho']

# # Para uma tuple se utiliza "()" e não "[]"
# var_cores_tuple = ('roxo', 'preto', 'branco', 'rosa')


# #Type para imprimir o tipo:
# # print(type(var_cores_list))
# # print(type(var_cores_tuple))

# print(var_cores_list)
# print(var_cores_tuple)


# var_duas_listas = var_cores_list * 2
# var_duas_listas2 = var_cores_tuple * 2

# print(var_duas_listas)
# print(var_duas_listas2)

# Arrays - utilizado para listas muito grande

