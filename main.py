slw= {'Marian': 123123123 , 'Marcin': 456456456 , 'Mateusz': 789789789}

slw.update({'Mikolaj': 576378567})
y= input("Podaj imie: ")
x= int(input("Podaj numer: "))

slw.update({y: x})

del slw['Marcin']

for i in slw:
    print(i , ' - ' , slw[i])