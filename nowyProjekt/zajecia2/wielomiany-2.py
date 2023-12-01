#napisz program ktory wczyta podstawe potegi oraz napis reprezetujacy wykladnik potegi w systemie binarnym a nastepnie wypisze wartosc potegi zasosuj funkcje ktora wykonalismy na lekcji
# def potega(podstawa, wykladnik):
#    x=bin(podstawa**wykladnik)
#
#    return x
#
# print(potega(3,2))
def bintodec(s):
    p=len(s)-1
    w=0
    for i in s:
        if i=='1':
            w=w+2**p
        p-=1
    return w
