#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

p=float((input('Primeiro segmeto: ')))
s=float((input('Segundo segmeto: ')))
t=float((input('Terceiro segmeto: ')))

if p < s + t and s < p + t and t < p + s:
    print('\nOs segmentos acima podem formar triângulo ! ')
else:
    print('\nOs segmentos acima NÃO podem formar triângulo ! ')