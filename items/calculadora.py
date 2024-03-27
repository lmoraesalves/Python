#calculadora

print('Bem vindo a sua calculadora.')
print('Você deseja fazer uma conta ou receber a tabuada?')
soma_tabuada = input('Tabuada = 1 , Conta = 2: ')
soma_tabuada = int(soma_tabuada)

while soma_tabuada != 1 and soma_tabuada != 2:
    print(f'\nDigite o número 1 ou 2')
    soma_tabuada = input('Tabuada = 1 , Conta = 2: ')


    if soma_tabuada == 2:

        operacao = input('Escolha a operação matemática (+, -, *, /): ')
        numero1 = input('Escolha3 o primeiro número: ')
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
                print(f'O resultado é: {numero1} + {soma} = {numero1+soma}')
        elif operacao == '-':
            for soma in range(11):
                print(f'O resultado é: {numero1} - {soma} = {numero1-soma}')
        elif operacao == '*':
            for soma in range(11):
                print(f'O resultado é: {numero1} * {soma} = {numero1*soma}')
        else:
            for soma in range(11):
                if soma != 0:
                    print(f'O resultado é: {numero1} / {soma} = {numero1/soma}')
            
print()
print('Obrigado por me utilizar.')