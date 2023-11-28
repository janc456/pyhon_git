#napisz program podajacy wynik obliczenia zamiany ulamka binarngo na liczbe dziesietna przy zamianie podajemy ilosc bitow na jakich jest zapisana podana liczba
def BinToFloat(n, ileBit=0):
    wynik = 0
    for i in range(2, ileBit+2):
        if n[i] == '1' or n[i] == '0':
            if n[i]=='1':
                wynik += 2 ** (-i + 1)
        else:
            return "ERROR"
    return wynik

print(0.1 - BinToFloat("0,000110011001100110011", 8 ))
print(0.1 - BinToFloat("0,000110011001100110011", 12 ))
print(0.1 - BinToFloat("0,000110011001100110011", 16 ))
#wartosc dokladna x= 0,1 w systemie dziesietnym jest rowna 0,1 oblicz jaki bedzie blad przy zapisie liczby 0,1 z wykorzystaniem 8 bitow 12 bitow i 16 bitow
#napisz program ktory obliczy wartosc sinusa=1 korzystajac ze wzoru sin1= 1-1/3!+1/5!+1/7!...  obliczenia wykonaj z dokladnoscia d 4 miesc po kropce dziesietnej