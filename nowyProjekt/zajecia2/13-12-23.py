#napisz funkcje sprawdzajaca czy dwa punkty leza po tej samej stronie prostej jak to obliczyc, podajemy wartosci a b i c roenania ogolnego


punkt=[(1,2),(3,4)]
def func(a,b,c,punkt):
    if (a*punkt[0][0]+b*punkt[0][1]+c)*(a*punkt[1][0]+b*punkt[1][1]+c)>0:
        return True
    else:
        return False

print(func(-1,2,-3,punkt))
def odc()