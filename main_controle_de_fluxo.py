#if, else e elif
'''
velocidade = input('Qual sua velocidade atual ? ')
velocidade = int(velocidade)

if velocidade > 100:
    print('Você está acima da velocidade.')
    
elif velocidade < 50:
    print('Você está abaixo da velocidade adequada.')

else:
    print('Você está na velocidade adequada.')
'''

# Teste com financiamento
'''
renda_acima_5mil = True
nome_limpo = False

#and dentro de um if é para que seja necessário que as 2 variaveis precisam ser verdadeiras
#or dentro de um if é para que seja necessário apenas 1 das afirmações verdadeiras

if renda_acima_5mil and nome_limpo:
    print('Financiamento aprovado!!')
    print('Parabéns!!!!')

else:
    print('Financiamento negado.')
'''

# Multiplos operadores de comparação
'''
valor = input('Por gentileza, digite o valor do produto: ')
valor = int(valor)

if 20 <= valor < 40:

#if valor >= 20 and valor < 40:
    print('Produto aceito para publicação.')

else:
    print('Produto negado para publicação.')
'''

