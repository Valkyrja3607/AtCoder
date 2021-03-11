n,m=map(int,input().split())
a=list(map(int,input().split()))
import collections
c=collections.Counter()
for j,i in enumerate(a):
    if c[i]==0:
        c[i]=[-1]
    c[i].append(j)

ans=10**10
cc=collections.Counter(a[:m])
for i in range(max(a[:m])+2):
    if cc[i]==0:
        ans=i
        break
if n==m:
    print(ans)
    exit()
cc=collections.Counter(a[-m:])
for i in range(max(a[-m:])+2):
    if cc[i]==0:
        ans=min(i,ans)
        break
for i in range(max(a)+2):
    if c[i]==0:
        print(min(i,ans))
        exit()
    for l,r in zip(c[i],c[i][1:]):
        if r-l>m:
            print(min(i,ans))
            exit()
print(ans)