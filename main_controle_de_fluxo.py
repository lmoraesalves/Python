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

#calculadora

print('Bem vindo a sua calculadora.')
print('Você deseja fazer uma conta ou receber a tabuada?')
soma_tabuada = input('Tabuada = 1 , Conta = 2: ')
soma_tabuada = int(soma_tabuada)

if soma_tabuada == 2:

    operacao = input('Escolha a operação matemática (+, -, *, /): ')
    numero1 = input('Escolha o primeiro número: ')
    numero1 = int(numero1)
    numero2 = input('Escolha o segundo número: ')
    numero2 = int(numero2)

    if operacao == '+':
        numerofinal = str(numero1 + numero2)
        print('O resultado é: ' + numerofinal)
    elif operacao == '-':
        numerofinal = str(numero1 - numero2)
        print('O resultado é: ' + numerofinal)
    elif operacao == '*':
        numerofinal = str(numero1 * numero2)
        print('O resultado é: ' + numerofinal)
    else:
        numerofinal = str(numero1 / numero2)
        print('O resultado é: ' + numerofinal)

else:
    operacao = input('Escolha a operação matemática (+, -, *, /): ')
    numero1 = input('Escolha o seu número para a tabuada: ')
    numero1 = int(numero1)
    if operacao == '+':
        for soma in range(11):
            print(f'O resultado é: + {numero1} + {soma} = {numero1+soma}')
    elif operacao == '-':
        for soma in range(11):
            print(f'O resultado é: + {numero1} - {soma} = {numero1-soma}')
    elif operacao == '*':
        for soma in range(11):
            print(f'O resultado é: + {numero1} * {soma} = {numero1*soma}')
    else:
         for soma in range(11):
            print(f'O resultado é: + {numero1} / {soma} = {numero1/soma}')


print('Obrigado por me utilizar.')