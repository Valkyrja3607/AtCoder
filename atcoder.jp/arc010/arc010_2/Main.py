n=int(input())
l=[31,29,31,30,31,30,31,31,30,31,30,31]
from itertools import accumulate
l=[0,0]+list(accumulate(l))
ll=[0]*367
for i in range(n):
    m,d=map(int,input().split("/"))
    day=l[m]+d
    ll[day]+=1
for i in range(1,367):
    if i%7<=1:
        ll[i]+=1

ans=0
tmp=0
c=0
for idx,i in enumerate(ll):
    if i!=0:
        tmp+=i
        ans=max(ans,tmp-c)
        c+=i-1
    elif c!=0:
        c-=1
        ans=max(ans,tmp-c)
    else:
        tmp=0
        c=0

print(max(ans,tmp-c))