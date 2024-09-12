compra = float(input('Insira o valor de compra: '))
desconto = int(input('Insira o valor do desconto: '))

valorFinal = compra - compra * (desconto / 100)

print('O valor final é: ', valorFinal)
