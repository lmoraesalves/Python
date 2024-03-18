# # Lambda Function
#     # Função pequena sem nome
#     # Pode ter vários argumentos, mas somente 1 exxpressão
#     # Muito utilizada dentro de outras funções
#     # Código mais 'clean'


# # def somar(var_x):
# #     return var_x + 10

# # print(somar(2))


# var_somar10 = lambda var_x, var_y: var_x + var_y + 10

# print (var_somar10(2, 4))


# # Lambda dentro de uma função


# def somar(x):
#     var_lambda = lambda x: x + 10 
#     return var_lambda(x) * 4

# print(somar(2))


### Build in functions #### Procurar no google.

# # Função MAP em uma lista
#     # Aplicar uma função a um Iterable, por item. (List, tuple, dic, etc..)

# var_list1 = [1, 2, 3, 4]


# def var_multi(x):
#     return x * 2

# var_list2 = map(var_multi, var_list1)

# print(list(var_list2))

# # Função Map com Lambda

# var_list1 = [1, 2, 3, 4]


# # def var_multi(x):
# #     return x * 2

# # var_list2 = map(lambda x: x * 2, var_list1)

# print(list(map(lambda x: x * 2, var_list1)))

# # Função Filter
#     # Similar ao map para rodar uma função dentro de uma lista, mas em vez de me dar o resultado, ela filtra resultado
#     # Muito ultilizado com listas

# var_valores = [10, 12, 34, 44, 57]

# # def remove20(x):
# #     return x < 20

# # # print (list(map(remove20, var_valores)))
# # # print (list(filter(remove20, var_valores)))

# print (list(map(lambda x: x > 20, var_valores)))
# print (list(filter(lambda x: x > 20, var_valores)))