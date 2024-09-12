v1 = int(input('Lado 1:'))
v2 = int(input('Lado 2:'))
v3 = int(input('Lado 3:'))

if(v1 + v2 > v3):
    if(v2 + v3 > v1):
        if(v1 + v3 > v2):
            print('É triângulo!')
            if(v1 == v2 and v1 == v3):
                print('Equilátero!')
            elif(v1 == v2 or v1 == v3 or v2 == v3):
                print('Isósceles!')
            elif(v1 != v2 and v1 != v3 and v2 != v3):
                print('Escaleno!')
        else:
            print('Não é triângulo!')
    else:
        print('Não é triângulo!')
else:
    print('Não é triângulo!')
