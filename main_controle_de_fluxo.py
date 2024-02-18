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
#For Loop (looping)
#imprimir de 1 a 5

#assim ele imprime de 0 a 4 pois trabalha com index
'''
for numero in range(5):
    print(numero)

for numero in range(0, 20, 5):
    print(numero)
'''

#for loop para string
'''
palavra = 'Espetacular'

for letra in palavra:
    print(f' {letra} está dentro da palavra {palavra}')
'''

#for loop com if/else
'''
compra_confirmada = True
dados_compra = 'Compra no Valor de R$12.50 e entrega confirmada'


for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados por e-mail.')
        break
else:
    print('Falha na compra, tente novamente.')
'''

#For Loop - Nested loops.
    #outer loop - de fora
    #inner loop - de dentro
'''
for numero1 in range(1, 6):
    print(f'Produto {numero1}')
    for numero2 in range(11):
        print(f'Produto {numero1} está no lote {numero2}')
'''

#Separando strings
# palavra = 'Fantástico'

# for space in palavra:
#     print(space, end=' ')

#criar um retângulo com um símbolo específico
#retângulo de 6x6
'''
linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()
'''

#while loop
#criar promoção para o produto no valor de R$100
'''
valor = float(100)
dia = 1

while valor > 20:
    dia += 0
    print(f'No dia {dia} o produto será vendido por R${valor}')
    valor -= 5
'''

#operador ternário
'''
idade = input('Informe sua idade: ')
idade = int(idade)

# if 100 > idade >= 16:
#     print('Voto permitido!')
# else:
#     print('Idade incorreta.')


resultado = 'Voto Permitido' if 100 > idade >= 16 else 'Voto não permitido'

print(resultado)
'''

#condições com while loop
#publicar um produto com comissão de 10% se for acima de R$20


# Modelo para analise sem break
 
# var_valor = int(input('Digite o valor do produto R$: '))
 
# while var_valor > 20:
#   var_valor = (var_valor * .1)+var_valor
#   print(f'O valor final do produto sera R$ {var_valor}')
#   var_valor = 0
 
# Modelo para analise com if
 
# var_valor = int(input('Digite o valor do produto R$: '))
 
# if var_valor > 20:
#   var_valor = (var_valor * .1)+var_valor
#   print(f'O valor final do produto sera R$ {var_valor}')

valor = int(input('Digite o valor do produto em reais: '))


while valor > 20:
    valor = (valor * .1) + valor
    print(f'O valor final do seu produto séra de R${valor}')
    break