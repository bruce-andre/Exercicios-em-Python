#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

a=float(input('Digite o ângulo que você deseja: '))

seno=math.sin(math.radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a, seno))

cosseno=math.cos(math.radians(a))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, cosseno))

tangente=math.tan(math.radians(a))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(a, tangente))