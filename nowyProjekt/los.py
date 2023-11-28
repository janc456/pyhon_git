from random import choices

def los(n):
    return choices((1,2,3,4,5,6), k=n)

def rzut(pkt, rzut_kostka):
    if rzut_kostka == 6:
        return pkt
    if rzut_kostka in (5,4):
        return pkt * 2
    if rzut_kostka == 3 or rzut_kostka == 2:
        return  pkt //2
    if rzut_kostka == 1:
        return 1


def rezultat(pkt, tab):
    for i in tab:
        pkt = rzut(pkt, i)
    return pkt

tab = los(3)
print(tab)
print(rezultat(100,tab))
