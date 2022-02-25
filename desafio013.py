# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

s=float(input('Digite o seu salário atual: R$'))

a=float(s*0.15)

sn=float(s+a)

print('O seu novo salario com aumento de 15% fica: R${:.2f}'.format(sn))