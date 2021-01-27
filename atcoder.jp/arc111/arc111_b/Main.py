n=int(input())
par=[-1 for i in range(400002)]
def root(a):
    if par[a]<0:
        return a
    else:
        return root(par[a])

def size(a):
    return -par[root(a)]

def connect(a,b):
    a=root(a)
    b=root(b)
    if a==b:
        return False
    if size(a)<size(b):
        a,b=b,a
    par[a]+=par[b]
    par[b]=a
    return True
import collections
c=collections.Counter()
s=set()
for i in range(n):
    a,b=[int(j) for j in input().split()]
    connect(a,b)
    c[a]+=1
    s.add(a)
    s.add(b)

ans=collections.Counter()
for i in s:
    ans[root(i)]+=c[i]
res=0
for i in ans:
    res+=min(ans[i],size(i))

print(res)