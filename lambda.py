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

# # List Comprehesion com Strings
#     # Mias simples de escrever
#     # Utilizado quando você precisa criar uma nova lista a partir de uma existente
#     # [Expressão for inten in itens]

# var_frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
# # var_frutas2 = []

# # for var_iten in var_frutas1:
# #     if 'n' in var_iten:
# #         var_frutas2.append(var_iten)

# var_frutas2 = [iten for iten in var_frutas1 if 'b' in iten]
# print (var_frutas2)


# # List Comprehesion com Integers

# # var_valores = []

# # for var_x in range(6):
# #     var_valores.append(var_x * 10)

# # print (var_valores)

# var_valores = [var_x * 10 for var_x in range(6)]
# print (var_valores)

# Generator Expressions
    # Uma forma mais ráída para listas, dicionários, etc..
    # Menos memória alocada
    # Valores em bytes


from sys import getsizeof

var_numeros = [var_x * 10 for var_x in range(10)]


print (type(var_numeros))
print (var_numeros)
print (getsizeof(var_numeros))

print ('-------------')
var_numeros = (var_x * 10 for var_x in range(10)) # Para generator expression, tira o "[]" e coloca p "()"

print (type(var_numeros))
print (list(var_numeros))
print (getsizeof(var_numeros))