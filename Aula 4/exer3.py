#AULA 4 EXER 3

#3) Elabore um programa que solicite uma frase ao usuário e escreva a frase
#toda em maiúscula. No mesmo programa exiba a frase sem espaços em branco.
#Dica use replace.

valorInserido = input('Digite uma palavra ou uma frase: ')
valorUpper = valorInserido.upper()


print(valorUpper.replace(' ', ''))
