valorHora = float(input('Digite da sua hora: '))
horasTrabalhadas = float(input('Digite quantas horas trabalhou: '))

salarioBruto = valorHora * horasTrabalhadas
inss = salarioBruto * (8 / 100)
impostoRenda = salarioBruto * (11 / 100)
sindicato = salarioBruto * (5 / 100)
descontos = inss + impostoRenda + sindicato
salarioLiquido = salarioBruto - descontos

print('Salário bruto: ', salarioBruto)
print('INSS: ', inss)
print('Imposto de Renda', impostoRenda)
print('Sindicato: ', sindicato)
print('Salário Líquido: ', salarioLiquido)
