
# Primeiro desafio!


# Ponto do steak
    # Usar If Else
    
# Criar um programa que dependendo da temperatura (Em Celsius) do steak, ele retorna o ponto de cozimento
# O Usuário deverá fornecer a temperatura

# Temperaturas - cozimento
# 120°F ou 48° C - Rare (Selada)
# 130°F ou 54° C - Medium Rare (Ao ponto para mal)
# 140°F ou 60° C - Medium (Ao ponto)
# 150°F ou 65° C - Medium Well (Ao ponto para bem)
# 160°F ou 71° C - Well Done (Bem passada)

# Método 1:
'''
print(f'Bem vindo a análise de ponto da carne')

var_temp = int(input(f'\nPor favor, digite a temperatura da carne: '))

if var_temp > 0 and var_temp < 150:

    if var_temp <= 48:
        print(f'Cozinhar por mais alguns minutos')

    elif var_temp >= 48 and var_temp <= 53:
        print(f'A carne está selada')

    elif var_temp >= 54 and var_temp <= 59:
        print(f'A carne está ao ponto para mal')

    elif var_temp >= 60 and var_temp <= 64:
        print(f'A carne está ao ponto')

    elif var_temp >= 65 and var_temp <= 70:
        print(f'A carne está ao ponto para bem')

    elif var_temp >= 71 and var_temp <= 75:
        print(f'A carne está bem passada')

    else:
        print(f'A carne queimou!')

else:
    print(f'Digite um número válido!')
'''

# Método 2: 

print(f'Bem vindo a análise de ponto da carne')

var_temp = int(input(f'\nPor favor, digite a temperatura da carne: '))

if var_temp > 0 and var_temp < 150:

    if var_temp < 48:
        print(f'Cozinhar por mais alguns minutos')

    elif var_temp in range(48, 53):
        print(f'A carne está selada')
    elif var_temp in range(54, 59):
        print(f'A carne está selada')
    elif var_temp in range(60, 64):
        print(f'A carne está selada')
    elif var_temp in range(65, 70):
        print(f'A carne está selada')
    elif var_temp in range(71, 75):
        print(f'A carne está selada')
    else:
        print(f'A carne queimou!')

else:
    print(f'Digite um número válido!')