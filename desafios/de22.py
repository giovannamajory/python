nome = str(input("Digite seu nome: "))
mais = nome.upper()
print('Nome em maiusculo: {}' .format(mais))

min = nome.lower()
print('Nome em minusculo: {}' .format(min))

seme = nome.split()
sita = len(nome.replace(" ", ""))
seme2 = len(seme[0])
print('Seu nome tem {} letras e o primeiro {}' .format(sita, seme2 ))
