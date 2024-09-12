velMax = float(input('Insira o valor da velocidade máxima: '))
velMot = float(input('Insira o valor que o veiculo passou: '))

dif = velMot - velMax

if(dif > 31):
    print('Multa Gravíssima: 7 pontos - R$574,62 ')
elif(dif <= 31 and dif >= 11):
    print('Multa média: 5 pontos - R$127,69')
elif(dif <= 10 and dif >= 1):
    print('Multa leve: 3 pontos - R$85,13')
else:
    print('Velocidade normal')
