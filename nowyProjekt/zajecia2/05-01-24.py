# pA=[0,0]
# pB=[4,3]
#
# for i in range(pA[0],pB[0]+1):
#     for j in range (pA[1],pB[1]+1):
#         print(i,j)
tmp = []
with open('../punkty.txt' , 'r') as file:
    for i in file:
        tmp.append(i.strip().split())
pkt = []
for i in tmp:
    t = []
    for j in i:
        t.append(int(j))
    p1 = [t[0] , t[1]]
    p1 = [t[2] , t[3]]
    pkt.append(t)

print(pkt)