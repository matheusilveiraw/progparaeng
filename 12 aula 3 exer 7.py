precoOriginal = float(input('Insira o preço do produto em R$: '))

desconto = precoOriginal * 0.2
precoComDesconto = precoOriginal - desconto

print('Você recebeu R$%.2f em desconto, o preço final do produto é: R$%.2f' % (desconto, precoComDesconto))
