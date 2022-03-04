#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
#A multa vai custar R$7,00 por cada Km acima do limite.

v=float(input('Qual é a velocidade atual do carro ? '))

if v>80:
    print('Você foi MULTADO ! Excedeu o limite permitido de 80KM/h')
    vx= (v-80) * 7
    print('Você deve pagar uma multa no valor de R${:.2f} '.format(vx))
else:
    print('Tenha um bom dia, dirija com cuidado ! ')