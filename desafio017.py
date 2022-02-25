#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#Calcule e mostre o comprimento da hipotenusa.
import math #OU from math import hypot

co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca) #Caso (from math import hypot) Pode tirar math.
print('A hipotenusa vai medir {:.2f}'.format(hi))
