pv = float(input("Valor do investimento inicial: "))
i = float(input("Rentabilidade: ")) / 100
n = float(input("Meses: "))

fv =  (pv * (1 + i)) ** n

print('O montante total é de: ', fv)
