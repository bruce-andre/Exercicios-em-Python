#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

x=float(input('Primeiro Valor: '))
y=float(input('Segundo Valor: '))
z=float(input('Terceiro Valor: '))
# Verificando quem é o menor
menor = x
if y < x and y < z:
    menor = y
if z < x and z < y:
    menor = z
# Verificando quem é o maior
maior = x
if y > x and y > z:
    maior = y
if z > x and z > y:
    maior = y

print('O menor valor digitando foi {}'.format(menor))
print('O maior valor digitando foi {}'.format(maior))
