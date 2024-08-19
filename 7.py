fv = float(input("Montante total desejado: "))
i = float(input("Rentabilidade: ")) / 100
n = float(input("Meses: "))

pv =  (fv) / ((1 + i) ** n)

print('o valor inicial investido deve ser: ', pv)
