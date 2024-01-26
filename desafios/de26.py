dig = str(input('Digite uma frase: '))
letra = dig.upper(). count('A') 
po1 = dig.upper(). find('A') +1
po2 = dig.upper(). rfind('A') +1

print('Quantas vezes aparece a letra A : {}' .format(letra))
print('Em que posição ela aparece a primeira vez? {}' .format(po1))
print('A última posição em que a letra A aparece é {}' .format(po2))
