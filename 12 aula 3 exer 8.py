valorOriginal = float(input('Insira o valor original: R$'))
desconto = float(input('Insira o valor do desconto [%]: '))

valorDesconto = valorOriginal * (desconto/100)
valorFinal = valorOriginal - valorDesconto

print('O desconto foi de R$%.2f no produto, o valor final ficou R$%.2f' % (valorDesconto, valorFinal))
