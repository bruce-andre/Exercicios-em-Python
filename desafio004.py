#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a=input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaço ? ',a.isspace())
print('É um numero ? ',a.isnumeric())
print('É alfabetico ? ',a.isalpha())
print('É alfanumerico ? ',a.isalnum())
print('Está em maiusculas ? ',a.isupper())
print('Está em minuscula ? ',a.islower())
print('Está capitalizada ? ',a.istitle())