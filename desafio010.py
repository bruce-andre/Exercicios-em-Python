# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar (CONSIDERE $ 1,00 = R$ 3,27)

x= float(input('Digite o valor em R$ que você tem na carteira: '))
y= float(x/3.27)

print('Você tem ${:.2f} '.format(y))