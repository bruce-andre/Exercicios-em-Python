# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

print('-=-' *20)
x=int(input('Em que número eu pensei de 0 à 5 ? '))
print('-=-' *20)

y = random.randrange(0,5)


if y == x:
    print('\nParabéns você ACERTOU !!! \nO número em que pensei foi {} '.format(y))
else: 
    print('\nVocê ERROU !!! \nO número em que pensei foi {} '.format(y))

