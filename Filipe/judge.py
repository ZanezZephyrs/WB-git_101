# a ideia é que o programa conte cada letra de uma frase ou palavra

sentenca = input ("Digite a sentença sem números assentos ou caracteres específicos: ")
sentenca = sentenca.lower()

letras = "abcdefghijklmnopqrstuvwxyz"
contador = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

numeros = [0,1,2,3,4,5,6,7,8,9]

for j in range(len(sentenca)):
    if sentenca[j] == " " or sentenca[j] in numeros:
        continue
    for i in range(len(letras)):
        if sentenca[j] == letras[i]:
            contador[i] += 1
            break

zerado = 0

for i in range(26):
    if contador[i] == 0:
        zerado += 1
        if zerado == 26:
            print("A sentença inserida não possui caracteres válidos")
        else:
            continue
    else:
        print (letras[i] + ":",contador[i])
