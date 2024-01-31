import math

def kivalaszt():
    prim = False
    n = 9999

    while prim != True:
        n+=1
        i = 2
        while i <= math.sqrt(n) and n%i !=0:
            i++
        prim = i > math.sqrt(n)
    print(n)
