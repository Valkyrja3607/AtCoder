n,q=map(int,input().split())

par=[-1 for i in range(n)]

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

for i in range(q):
    a,b,c=map(int,input().split())
    if a==0:
        connect(b,c)
    else:
        if root(b)==root(c):
            print(1)
        else:
            print(0)