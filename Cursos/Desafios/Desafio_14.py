# -*- coding: utf-8 -*-

'''
criar um loop que imprima de 1 a 5 e pare com break,
depois criar um loop que imprima número de 1 a 10.
'''

print('Loop com break')
for numero in range(1, 5):
    if numero > 5:
        break
    print(numero)

print('Loop com continue')
for numero in range(1, 11):
    if numero == 5:
        continue
    print(numero)