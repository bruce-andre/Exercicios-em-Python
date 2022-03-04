#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

x=float(input('Qual é a distância da sua viagem ? '))

y=x*0.50
z=x*0.45

if x<=200:
    print('Você pagará um valor de R${:.2f} na sua passagem'.format(y))
else:
    print('Você pagará um valor de R${:.2f} na sua passagem'.format(z))
