v1 = int(input('Valor 1:'))
v2 = int(input('Valor 2:'))
v3 = int(input('Valor 3:'))

if(v1 > v2 and v1 > v3):
    print(v1, 'é o maior!')
elif(v2 > v1 and v2 > v3):
    print(v2, 'é o maior!')
elif(v3 > v1 and v3 > v2):
    print(v3, 'é o maior!')
else:
    print('há valores iguais, nenhum é o maior')

if(v1 < v2 and v1 < v3):
    print(v1, 'é o menor!')
elif(v2 < v1 and v2 < v3):
    print(v2, 'é o menor!')
elif(v3 < v1 and v3 < v2):
    print(v3, 'é o menor!')
else:
    print('há valores iguais, nenhum é o menor')
