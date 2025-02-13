''''
Criar um programa que calcule a quantidade de tinta necessária
para pintar uma parede. O usuário deverá fornecer as seguintes informações:
-Rendimento
-Altura
-Largura
O progama deverá calcular e mostrar quantas latas de tintas serão necessárias.
'''

rendimento = int(input('Qual é o rendimento da sua lata de tinta? '))
altura = int(input('Qual a altura da parede? '))
largura = int(input('Qual a largura da parede a ser pintada? '))

def calculo_tinta():
    area = altura * largura
    total =  area / rendimento
    print(f'Você necessita de {total} latas de tinta')

calculo_tinta()