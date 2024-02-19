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



#Argumento default e non-default
def var_boasvindas(nome, quantidade=6):
    print(f'Olá {nome}')
    print(f'Temos {str(quantidade)} de laptops em estoque.')

var_boasvindas('Lucas')