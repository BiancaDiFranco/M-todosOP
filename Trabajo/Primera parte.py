def num_primo (largo):
    primos = [2]
    numero = 1 
    while largo>len(primos):
        numero=numero+1
        for i in primos:
            if numero%i==0:
                break
            elif i>=numero**0.5:
                primos.append(numero)
                break
    return primos[-1]
