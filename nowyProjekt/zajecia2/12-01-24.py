# Napisz program, ktory wczyta tekst oraz wzorzec,
# zapisane malymi literami alfabetu lacinskiego,
# a nastepnie wyszuka wzorzec w tekscie,
# stosujac algorytm naiwny.
# W programie utworz funkcje funkcji znajdz.
tekst= 'gdfghjdhgvbjhhgfgxchjgj'
wzorzec = 'gdf'
# def func(tekst,wzorzec):
#     dlg_tekst = len(tekst)
#     dlg_wzorz = len(wzorzec)
#     for i in range(dlg_tekst-dlg_wzorz +1):
#         if tekst[i:i+dlg_wzorz] == wzorzec:
#             return True
#         return False
# result = func(tekst,wzorzec)
# print(result)
# def znajdz(w, t):
#     dw = len(w)
#     dt = len(t)
#     p = 0
#     while p <= dt - dw:
#         i = 0
#         while i<dw and w[i]==t[p+i]:
#             i+=1
#         if i == dw:
#             return p
#         else:
#             p+=1
#     return -1
lt=[]
lw = []

def func1 (wzorzec, tekst):
    for i in range(len(tekst)):
        lt.append(ord(tekst[i]))

    print(sum(lt))
    for i in range(len(wzorzec)):
        lw.append(ord(wzorzec[i]))

    print(sum(lw))
print(func1(wzorzec,tekst))
