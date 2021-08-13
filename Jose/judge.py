def sum(first_int, sec_int):
    s = first_int + sec_int
    return s

def product(first_int, sec_int):
    p = first_int * sec_int
    return p

def MMC(first_int, sec_int):
    mdc = MDC(first_int, sec_int)
    if mdc == None:
        return None
    else:
        mmc = (first_int*sec_int)/mdc
        return mmc

def MDC(first_int, sec_int):
    mdc = 1
    primos = [2, 3, 5, 7,  11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373]
    f_i = first_int
    s_i = sec_int
    dic_f_i = {}
    dic_s_i = {}
    i = 0 # servirá de identação para checar os numeros primos
    while(f_i > 1):
        while(f_i % primos[i] == 0):
            f_i = f_i/primos[i]
            if primos[i] not in dic_f_i:
                dic_f_i[primos[i]] = 1
            else:
                dic_f_i[primos[i]] += 1
        i += 1
    i = 0
    while(s_i > 1):
        while(s_i % primos[i] == 0):
            s_i = s_i/primos[i]
            if primos[i] not in dic_s_i:
                dic_s_i[primos[i]] = 1
            else:
                dic_s_i[primos[i]] += 1
        i += 1
    i = 0
    for i in range(len(primos)):
        if primos[i] not in dic_f_i or primos[i] not in dic_s_i:
            break
        if dic_f_i[primos[i]] > dic_s_i[primos[i]]:
            mdc = mdc * (primos[i] * dic_s_i[primos[i]])
        else:
            mdc = mdc * (primos[i] * dic_f_i[primos[i]])
    if i == 0:
        return None
    else:
        return mdc

def main():
    print("Insira os números a serem utilizados:")
    first_int = int(input())
    sec_int = int(input())
    s = sum(first_int, sec_int)
    print("Soma:")
    print(s)
    p = product(first_int, sec_int)
    print("Produto:")
    print(p)
    mmc = MMC(first_int, sec_int)
    if mmc == None:
        print("O MMC destes números não existe.")
    else:
        print("MMC:")
        print(mmc)
    mdc = MDC(first_int, sec_int)
    if mdc == None:
        print("O MDC destes números não existe.")
    else:
        print("MDC:")
        print(mdc)

main()
