caractere = input('Digite uma caractere: ').lower()

if caractere == 'a' or caractere == 'e' or caractere == 'i' or caractere == 'o' or caractere == 'u':
    print('Vogal!')
elif caractere == 'b' or caractere == 'c' or caractere == 'd' or caractere == 'f' or caractere == 'g' or caractere == 'h' or caractere == 'j' or caractere == 'k' or caractere == 'l' or caractere == 'm' or caractere == 'n' or caractere == 'p' or caractere == 'q' or caractere == 'r' or caractere == 's' or caractere == 't' or caractere == 'v' or caractere == 'w' or caractere == 'x' or caractere == 'y' or caractere == 'z':
    print('Consoante!')
else:
    print('Não é uma letra!')
