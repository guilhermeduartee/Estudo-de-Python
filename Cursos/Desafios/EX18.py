import math
#EX18
#faça um programa que leia um ângulo qualquer e mostre na tela o 
#valor do seno, cosseno e tangente desse angulo.
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print('O angulo de {} tem SENO de {}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem COSSENO de {}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print( 'O angulo de {} tem TANGENTE{}'.format(ângulo, tangente))