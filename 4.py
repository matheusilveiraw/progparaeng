n1 = int(input('Digite o valor a ser dividido: '))
n2 = int(input('Digite o valor que vai dividir: '))


try:
    print(n1, ' / ', n2,' = ', n1/n2)
except ZeroDivisionError:
    print('Divisão por zero inválida!')
