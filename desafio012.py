# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

po= float(input('Digite o valor do preço original: R$'))

pd= float(po*0.05)

pn= float(po-pd)

print('O valor desse produto com o desconto de 5% fica: R${:.2f} '.format(pn))