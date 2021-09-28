# crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dolares ela pode comprar
# valor do dolar US$1 = R$ 3,27

valor = float(input('Quanto dinheiro você tem? :'))
print('Você poderá obter esse valor {:.2f} em dolares'.format(valor/3.27))
