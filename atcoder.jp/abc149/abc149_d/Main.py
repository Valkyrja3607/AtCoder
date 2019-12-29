n,k=[int(j) for j in input().split()]
s,p,r=[int(j) for j in input().split()]
t=input()
ans=0
from itertools import*
for i in range(k):
    l=[]
    for j in range(-(-n//k)):
        tmp=i+k*j
        ss=""
        if tmp<n:
            l.append(t[tmp])
    for i,j in [(k,len(list(v))) for k,v in groupby(l)]:
       ans+=eval(i)*-(-j//2)

print(ans)