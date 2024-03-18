# Python Object-Oriented Programming

# Classes
    # Utiizadas para criar Objetos (Instances)
    # Objetos são partes dentro de uma class (Instancias)
    # Classes são utilizadas para agrupar dados e funções podendo reutilizar
    # ========
    # Class: Frutas
    # Objects: Abacate: Banana...

# class Funcionaros:
#     var_nome = 'Anna'
#     var_sobrenome = 'Oliveira'
#     var_data_nasc = '07/01/2000'

# var_user1 = Funcionaros () # É o primeiro obrigado

# print (var_user1.var_nome, var_user1.var_sobrenome)
# print (var_user1.var_data_nasc)


# # Criar a classe 

# class Funcionaros:
#     pass

# # Criar o Objeto
# var_user1 = Funcionaros()
# var_user2 = Funcionaros()

# # Criar os parâmetros do usuário1

# var_user1.nome = 'Anna'
# var_user1.sobrenome = 'Oliveira'
# var_user1.data_nascimento = '07/01/2000'

# # Imprimir
# print (var_user1.nome, var_user1.sobrenome)


# # Criar os parâmetros do usuário2

# var_user2.nome = 'Lucas'
# var_user2.sobrenome = 'Alves'
# var_user2.data_nascimento = '08/07/1995'

# # Imprimir
# print (var_user2.nome, var_user2.sobrenome)


# Criando Construtores

class Funcionaros:

    def __init__(self, nome, sobrenome, data_nasc):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nasc = data_nasc

# Criar o Objeto
var_user1 = Funcionaros('Anna', 'Oliveira', '08/01/2000')
var_user2 = Funcionaros('Lucas', 'Alves', '08/07/1995')
var_user3 = Funcionaros('Sophia', 'Hadassa', '18/07/2017')

print(var_user1.nome, var_user1.sobrenome, var_user1.data_nasc)
print(var_user2.nome, var_user2.sobrenome, var_user2.data_nasc)
print(var_user3.nome, var_user3.sobrenome, var_user3.data_nasc)


