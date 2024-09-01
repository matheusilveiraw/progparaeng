#8) Desenvolva um programa que leia uma frase e um caractere. Em seguida,
#exiba ambos e o número de ocorrências do caractere na frase.

fraseInserida = input('Digite uma frase: ')
caractereOcorrencia = input('Digite um caractere: ')

print('Na frase', fraseInserida, 'a caractere', caractereOcorrencia, 'aparece', fraseInserida.count(caractereOcorrencia))
