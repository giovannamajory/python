n1 = str(input('Digite um número de 0 a 9999: '))
n1.split()

#lista = [0, 1, 2, 3]

unidade = n1[3]
dezena = n1[2]
centena = n1[1] 
milhar = n1[0]

print("""Unidade: {}
Dezena: {}
Centena: {}
Milhar: {} """ .format(unidade, dezena, centena, milhar)) 
