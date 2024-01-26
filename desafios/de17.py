import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h1 = math.hypot(co, ca)
print('A hipotenusa vale {:.2f}' .format(h1))
