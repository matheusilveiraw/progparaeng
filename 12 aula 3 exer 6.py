#faz 20km/l
#1l = 4,95
precoCombustivel = 4.95

dindin = float(input('Quanto dinheiro será gasto com gasolina?'))

combustivel = dindin / precoCombustivel
kmsPercorridos = 20 * combustivel

print('Com R$%.2f, você terá %.1f litros e poderá percorrer %.0fkms' % (dindin, combustivel, kmsPercorridos))
