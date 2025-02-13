'''
Criar um programa que gere 3 listas de acordo com a necessidade logo abaixo:

1- Lista1 = Funcionários que tem carro e trabalham a noite
2- Lista2 = Funcionários que tem carro e trabalham durante o dia
3- Lista3 = Funcionários que não tem carro

'''

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

#Lista1                #Busca o semelhante
lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

#Lista2                #Busca o semelhante
lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

#Lista3                    #Busca diferença
lista3 = set(funcionarios).difference(tem_carro)
print(lista3)