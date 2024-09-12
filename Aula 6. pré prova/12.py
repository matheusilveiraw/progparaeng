12.
nota1 = float(input('Nota 1:'))
nota2 = float(input('Nota 2:'))

media = (nota1 + nota2) / 2

if(media == 10):
    print('Aprovado com distinção!')
elif(media < 10 and media >= 7):
    print('Aprovado!')
else:
    print('Reprovado!')
