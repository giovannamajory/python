print('Vamos descobrir quanto de tinta você precisa!')
l = float( input('Me diga a largura de sua parede: '))
a = float( input('Me diga a altura de sua parede: '))
m = a * l
t = m / 2
print('Sua parede tem a dimensão de {} x {} e a área de {}m²'.format(l, a, m))
print('Para pintar essa parede, você precisara de {} litros de tinta' .format(t))
