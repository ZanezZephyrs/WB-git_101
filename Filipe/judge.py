# a ideia é que o programa conte cada letra de uma frase ou palavra

sentenca = input ("Digite a sentença sem números, assentos ou caracteres específicos: ")
sentenca = sentenca.lower()

letras = "abcdefghijklmnopqrstuvwxyz"

dicionario = {letra:0 for letra in letras}

numeros = [0,1,2,3,4,5,6,7,8,9]

for j in range(len(sentenca)):
    if sentenca[j] == " " or sentenca[j] in numeros:
        continue
    for (letra) in dicionario.keys():
        if sentenca[j] == letra:
            dicionario[letra] += 1
            break

zerado = 0

for (letra,contador) in dicionario.items():
    if contador == 0:
        zerado += 1
        if zerado == 26:
            print("A sentença inserida não possui caracteres válidos")
        else:
            continue
    else:
        print (letra + ":",contador)
