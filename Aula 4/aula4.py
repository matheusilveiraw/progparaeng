#4) Desenvolva um programa que solicite uma frase ao usuário e escreva a frase
#invertida. Dica [::-1]

valorInserido = input('Digite uma palavra ou frase: ')
novaString = ''

for i in range(len(valorInserido) - 1, 0, -1):
    novaString += valorInserido[i]

print(novaString)
