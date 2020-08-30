n,m=map(int,input().split())
par=[-1 for i in range(n+1)]
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

for i in range(m):
    a,b=map(int,input().split())
    connect(a-1,b-1)
ans=0
for i in par:
    if i<0:
        ans=max(ans,-i)
print(ans)