n=int(input())
sp=[]
for i in range(n):
    a=input().split()
    sp.append([a[0],int(a[1]),i+1])

l=[[] for i in range(n)]
from operator import itemgetter
sp.sort(key=itemgetter(1))
sp.reverse()
sp.sort(key=itemgetter(0))

for i in range(n):
    print(sp[i][2])