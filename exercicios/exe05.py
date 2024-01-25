nome = input('Olá, qual é o seu nome? ')
print ('Prazer em te conhecer {}!' .format(nome))
print ('A seguir vamos descobrir algumas coisas sobre números. Para isso escolha dois números!')
n1 = int(input('Um valor: '))
n2 = int(input('Outro Valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
sub = n1 - n2
p = n1 ** n2
rd = n1 % n2
di = n1 // n2
print('A soma é {}, \n a multiplicação é {}, a divisão é {}, a subtração é {}' .format(s, m, d, sub))
print('A divisão inteira é {}, a potencia é {} e o módulo é {}' .format(di, p, rd))
 