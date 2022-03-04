#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome=str(input('Digite seu nome completo: ')).strip() 
x= nome.split()

print('Seu primeiro nome é {}'.format(x[0]))
print('Seu último nome é {}'.format(x[len(x)-1]))