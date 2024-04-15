
# Desafios com funções

'''
Criar um programa que calcula a quantidade de tinta necessária paa pintar uma parde. O usuário deverá fornecer
as seguintes informações:
    Rendimento;
    Altura;
    Largura.

O programa defe mostrar na tela a mensagem 'Você necessita de "x" latas de tintas
'''

var_rend = int(input('Qual é o rendimento da lata? '))
var_alt = int(input('Qual é a altura da parede? '))
var_larg = int(input('Qual é a largura da parede? '))


def calculo_tinta():
    area = var_alt * var_larg
    total = area / var_rend
    print(f'Você preisa de {total} latas de tinta')

calculo_tinta()

