# faça um algoritmo que leia o preço e mostre seu novo preço com desconto de 5%

valor = float(input('Entre com o valor do produto R$ '))
valor_final = valor - (valor * 0.05)
print('O valor final do produto é {:.2f}'.format(valor_final))
