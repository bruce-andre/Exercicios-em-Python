#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d=float(input('Quantos dias alugados ? '))
k=float(input('Quantos Km rodados ? '))

c=float(d*60)
kr=float(k*0.15)

print('O total a pagar é de R${:.2f}'.format(c+kr))