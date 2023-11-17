#napisz program ktory obliczy wartosc sinusa=1 korzystajac ze wzoru sin1= 1-1/3!+1/5!+1/7!...  obliczenia wykonaj z dokladnoscia d 4 miesc po kropce dziesietnej
eps = 0.00001

skladowa = 1
i = 1
wynik= 0
while skladowa>eps:
    i += 2
    wynik += skladowa / i
    skladowa /= i
    print(skladowa)

