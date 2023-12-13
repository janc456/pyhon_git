from math import sqrt

punkty1 = [(2,3),(1,7)]

def dlugosc(punkty):
    x1, y1 = punkty[0]
    x2, y2 = punkty[1]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(dlugosc(punkty1))