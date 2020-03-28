n=int(input())
a=[]
for i in range(n-1):
    a.append([0]*(i+1)+[int(j) for j in input().split()])

def base(X,n=3):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out
import itertools
ans=-10**18
for i in range(3**n):
    tmp=0
    b=base(i).rjust(n,"0")
    l=[[],[],[]]
    for p,q in enumerate(b):
        l[int(q)].append(p)
    for ll in l:
        for p,q in itertools.combinations(ll,2):
            p,q=min(p,q),max(p,q)
            tmp+=a[p][q]
    if ans<tmp:
        ans=tmp

print(ans)






