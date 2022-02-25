# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la.
# sabendo que a cada litro de tinta,pinta uma área de 2m²

l=float(input('Digite a largura da sua parede em metros: '))
a=float(input('Digite a altura da sua parede em metro: '))

m=float(l*a)
t = m/2

print('\n')
print('A largura da sua parede é {} metors \nE a altura é {} metros \n \nEntão você precisa de {} M² \nEntão você vai precisar de {} litros de tinta para pintar sua parede'.format(l,a,m,t))