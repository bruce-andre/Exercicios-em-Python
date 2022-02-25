# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input('Digite um número: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = float(n1) ** 0.5
print('O numero que você digitou foi: {} \n O dobro é {} \n O triplo é {} \n E sua raiz é {} '.format(n1,dobro,triplo,raiz))