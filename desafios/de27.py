'''
Faça um progama que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separamente

'''

nome = str(input('Digite seu nome: ')).strip()
n = nome.split()

print('Prazer em te conhecer!')
print('Seu primeiro nome é {}' .format(n [0]))
print('Seu último nome é {}' .format(n [-1]))
