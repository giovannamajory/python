print('Olá, somos um loja virtual que possui 5 porcento (%) de desconto em toda nossa loja!')
v = float( input('Coloque aqui o preço da(s) peça(s): '))
d = 5 / 100 * v
vf = v - d
print ('Com o desconto da nossa loja você economizou {:.2f}! Total a pagar {}' .format(d, vf))
