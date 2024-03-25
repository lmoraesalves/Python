# Functions (Funções)
#     #DRY - Don't repeat yourself.

# def boas_Vindas():
#     print('Olá Lucas')
#     print('Temos cincos laptops em estoque.')

# boas_Vindas()

# Função de soma!!

# def var_soma_2_num():
#     numero1 = 10
#     numero2 = 5
#     resultado = numero1+numero2
#     print(resultado)

# var_soma_2_num()

#parâmetro e argumento
# def var_boasvindas(nome, quantidade):
#     print(f'Olá {nome}')
#     print(f'Temos {str(quantidade)} de laptops em estoque.')

# var_boasvindas('Lucas', 10)
# var_boasvindas('Anna', 5)
# var_boasvindas('Theo', 3)


# def var_boasvindas_lucas():
#     print('Olá Lucas')

# def var_boasvindas_anna():
#     print('Olá Anna')

# def var_boasvindas_theo():
#     print('Olá Theo')

# var_boasvindas_lucas()
# var_boasvindas_anna()
# var_boasvindas_theo()



# #Argumento default e non-default
# def var_boasvindas(nome, quantidade=6):
#     print(f'Olá {nome}')
#     print(f'Temos {str(quantidade)} de laptops em estoque.')

# var_boasvindas('Lucas')

# def cliente1(nome):
#     print(f'Olá {nome}')


# def cliente2(nome):
#     return f'Olá {nome}'


# x = cliente1('Lucas')
# y = cliente2('Anna')

# print(y)
# print(x)

#criar função que soma vários números

# def soma(*var_numeros):
#     var_result = 0
#     for var_num in var_numeros:
#         var_result += var_num
#     return var_result


# var_x = soma(2, 3, 4, 7)
# print(var_x)

# #Vários argumentos xargs nomeando parâmetros

# def agencia(**carro):
#     return carro

# print(agencia(marca='Gol', cor='Branco', motor=1.0, placa=1234))


#importando os módulos
#Qual o número fatorial de 4

# import math

# print(math.factorial(57))