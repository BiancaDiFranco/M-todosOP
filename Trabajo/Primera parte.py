noprimos = []
primos = []
def num_primo (n):
    n = int(input("Ingrese un numero entero"))
    for divisor in range (2, n + 1):
        if n % 2 == 0: 
            noprimos.append(n)
        elif n/divisor != 0:
            resultado = n/divisor
            primos.append(resultado)
            print(primos)
            return num_primo