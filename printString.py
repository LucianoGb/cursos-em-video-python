m = 'menu'
print('Espaço de 20 caracteres {:20}!'.format(m))
# saida - Espaço a direito menu                !

#alinhado a direita
print('Espaço a direita {:>20}!'.format(m))
# saida - Espaço a direito                 menu!

print('Espaço a esquerda {:<20}!'.format(m))
# saida - Espaço a direito menu                !

print('Espaço centralizado {:^20}!'.format(m))
# saida - Espaço centralizado         menu        !

print('Espaço centralizado com sinal de igual em volta {:=^20}!'.format(m))
# saida - Espaço centralizado com sinal de igual em volta ========menu========!