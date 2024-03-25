# # Dicionários
#     # Utiliza o index no formato de keys e values
#     # aceita strings, integer, float, boolean...

# var_aluno = {'nome': 'Anna', 'idade': 24, 'nota_final': 'A', 'aprovação': True}

# print(var_aluno['nome'])

# # Manipular dados no dicionário

# var_aluno = {'nome': 'Anna', 'idade': 24, 'nota_final': 'A', 'aprovação': True}

# # var_aluno['nome'] = 'Lucas'
# # var_aluno.update({'nome': 'Lucas', 'idade': 28, 'nota_final': 'B'})
# # var_aluno.update({'endereço': 'Rua A'})

# del var_aluno['aprovação'] # Para remover

# print(var_aluno)
# print()
# print(var_aluno['nome'])
# print()
# print(var_aluno.get('endereço', 'Não existe'))

# # Looping dentro de dicionários:

# var_aluno = {'Nome:': 'Anna', 'Idade:': 24, 'Nota_final:': 'A', 'Aprovação:': True}

# for var_keys, var_values in var_aluno.items():
#     print (var_keys, var_values)


# var_aluno = {
#     'nome': 'Anna', 
#     'idade': 24, 
#     'nota_final': 'A', 
#     'aprovação': True, 
#     'Matérias': [
#         'Matemática', 
#         'Física',
#         'Inglês'
#         ]
# }


# # print(var_aluno)
# # print(  )
# # print(var_aluno.get('Matérias'))
# # print(  )
# # print(len(var_aluno))

# print(var_aluno.items())
# print(var_aluno.keys())
# print(var_aluno.values())

