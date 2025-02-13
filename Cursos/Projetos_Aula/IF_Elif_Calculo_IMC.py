#Calculo de IMC

'''
Qual é a sua altura em cm: 
Qual é o seu peso em Kg:
'''

# MENOR QUE 18,5       MAGREZA
# ENTRE 18,5 E 24,9    NORMAL
# ENTRE 25,0 E 29,9    SOBREPESO
# ENTRE 30,0 E 39,9    OBESIDADE
# MAIOR QUE 40         OBESIDADE GRAVE

altura = float(input('Qual a sua altura:'))
peso = float(input('Qual o seu peso em Kg: '))

IMC = peso / (altura/100)**2

print(IMC)

if IMC < 19.5:
    print('Magreza')
elif IMC >= 18.5 and IMC < 24.9:
    print('Normal')
elif IMC >= 25.0 and IMC < 29.0:
    print('Sobrepeso')
elif IMC >= 30.0 and IMC < 39.9:
    print('Obesidade')
else:
    print('Obesidade grave!')