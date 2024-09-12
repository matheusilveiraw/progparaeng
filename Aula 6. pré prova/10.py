10.

pesoPeixe = float(input('Peso pescado: '))

if(pesoPeixe > 50):
    quilosMais = pesoPeixe - 50
    print('A multa é de: ', quilosMais*4.00)
else:
    print('Não paga multa')
