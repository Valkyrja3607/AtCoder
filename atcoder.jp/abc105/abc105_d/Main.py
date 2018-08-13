import collections

n,m=map(int,input().split())
a=[int(i) for i in input().split()]

s=0
ans=0
l=[]

for i in a:
    s+=i
    l.append(s%m)

c=collections.Counter(l)

for p,q in c.items():
    if int(p)==0:
        ans+=q*(q+1)//2
    else:
        ans+=q*(q-1)//2


print(ans)