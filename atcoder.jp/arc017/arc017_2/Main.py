n,k,*a=map(int,open(0).read().split())
if k==1:
    print(n)
    exit()
l=[]
for i,j in zip(a,a[1:]):
    if i<j:
        l.append(1)
    else:
        l.append(0)

from itertools import*
g=[[k,len(list(v))]for k,v in groupby(l)]
ans=0
for i,j in g:
    if i==1:
        ans+=max(0,j-k+2)
print(ans)