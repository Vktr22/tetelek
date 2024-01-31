import math
szam = 2;

def osztok(szam):
    list = [];
    for i in range(2, round(math.sqrt(szam)+1)):
        if szam % i == 0:
            list.append(i);
    return list;
print(osztok(36));                                  #eldontes tetele

def osztok2(szam):
    list = [];
    i = 0;
    while i >= 2 and i <= round(math.sqrt(szam)+1):
        if szam % 1 == 0:
            list.append(i)
        i +=1
    return list;