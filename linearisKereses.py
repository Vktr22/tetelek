

def linKer():
    also = 42;
    felso = 67;
    i = also;
    
    while i <= felso and i%10 != 0:
        i++;
    bool:van = i <= felso;
    if(van):
        print("van 0-ra végződő szám: "+i)
    else:
        print(" nincs 0-ra végződő szám")
