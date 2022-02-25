# Escreva um programa que leia um valor em metros e o exiba convertudo em centimetros e milimetros.
m=float(input('Digite um valor: '))
c= m*100
mm= m*1000
print('O valor {} em metros correponde em : \n {:.0f} Centimetros \n {:.0f} Milimetros'.format(m,c,mm))
