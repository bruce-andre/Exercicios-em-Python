# Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.

nome=input('Digite o seu nome: ')

nome1= nome.upper()
print('Seu nome em maiúsculas é {}'.format(nome1))

nome2= nome.lower()
print('Seu nome em minúsculas é {}'.format(nome2))

nome3= len(nome.strip())
print('Seu nome tem ao todo {} letras'.format(nome3))

nome4= nome.split()
print('Seu primeiro nome é "{}" e ele tem "{}" letras '.format(nome4[0], len(nome4[0])))