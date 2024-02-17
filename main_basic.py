''' #Print test no console

print('teste')

#print variable

x = 2

print(x)

'''

#variables
'''
x = str(3)
y = int(4)
z = float(5)

print(x + x)
print(y + y)
print(z + z)
'''


#O Lucas tem 28 anos e mora em barueri
'''
nome = 'Lucas'
idade = 28
idade = str(idade)
cidade = 'Barueri' 

print('O ' + nome + ' com a idade de ' + idade + ' e mora na cidade de '  + cidade + '.')
'''


#adicionando input
'''
nome = input('Qual o seu nome: ')
nasc = input('Qual é o seu ano de nascimento: ')
ano = int(2024) - int(nasc)
ano = str(ano)

print('O seu nome é: ' + nome + ' e você tem ' + ano + ' anos de idade.')
'''


#usando slice
'''
valor = 99.75
valor = str(valor)
#index  01234

print('centavos ' + valor[3:5])
'''


#Formated String
'''
nome = 'Marcos'
sobrenome = 'Silva'
profissao = 'programador'

texto = 'O ' + nome + ' ' + sobrenome + ' é um excelente ' + profissao + '.'

print(texto)

texto2 = f'O {nome} {sobrenome} é um excelente {profissao}.'

print(texto2)
'''


#metods for string
'''
mensagem = 'eu adoro churrasco.'
#index      0123456789

print(mensagem.strip())
'''