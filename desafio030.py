#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

x=int(input('Digite um número: '))

y= x % 2

if y == 0:
    print('O número {} é PAR'.format(x))
else:
    print('O número {} é ÍMPAR'.format(x))