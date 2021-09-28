# faça um programa que leia algo e moestre o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite alguma coisa ')
print('É um alpha numérico: ',algo.isalnum())
print('É alpha: ', algo.isalpha())
print('É ascii: ', algo.isascii())
print('É digito: ',algo.isdigit())
print('É minúsculo: ',algo.islower())
print('É número: ',algo.isnumeric())
