'''
faça um programa que leia a largura e altura de uma parede em metros
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2m²
'''

h = float(input('Digite a altura da parede: '))
b = float(input('Digite o comprimento da parede: '))

area = b * h

quantidade_de_litros = area / 2

print('A quantidade necessária de litros em tinta para pintar a parede é {:.2f}'.format(quantidade_de_litros))
