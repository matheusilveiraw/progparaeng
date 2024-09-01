#7) Elabore um programa que leia o nome do usuário e mostre o nome de traz
#para frente, utilizando somente letras maiúsculas.

nomeCompleto = input('Digite uma palavra ou frase: ')
novaString = ''

for i in range(len(nomeCompleto) - 1, 0, -1):
    novaString += nomeCompleto[i]

print(novaString.upper())
