custoCapa = 24.95 * 0.35
transporte1 = 3
transporteRes = 0.75

nLivros = int(input("Digite o número de livros: "))

valorTotal = (custoCapa * nLivros) + (transporte1 + ((nLivros - 1) * transporteRes))

print('O valor total é', valorTotal)

