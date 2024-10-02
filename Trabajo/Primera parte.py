

n = int(input("Ingrese un numero entero"))
def num_primo (n):
    primos = []
    i = 1 
    while n< len(primos):
        for a in range (i):
            a+=2
            if i%a==0 and a<i:
             break 
            elif a==i:
                num_primo.append(i)
            
    return primos[-1]    
num_primo(n)
