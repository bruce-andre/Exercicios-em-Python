#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

s=float(input('Qual é o salário do funcionário ? R$'))

if s<= 1250.00:
    a=float(s*0.15)
    sn=float(s+a)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(s,sn))
else:
    if s> 1250.00:
        ab=float(s*0.10)
        abc=float(s+ab)
        print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(s,abc))
