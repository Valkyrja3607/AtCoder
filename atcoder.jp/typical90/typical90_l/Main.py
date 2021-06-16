h,w=map(int,input().split())
par=[-1 for i in range(h*w)]
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

s=set()
for i in range(int(input())):
    q=[int(i)-1 for i in input().split()]
    if q[0]==0:
        r,c=q[1:]
        s.add(r*w+c)
        if (r+1)*w+c in s and r+1<h:
            connect(r*w+c,(r+1)*w+c)
        if (r-1)*w+c in s and 0<=r-1:
            connect(r*w+c,(r-1)*w+c)
        if r*w+c+1 in s and c+1<w:
            connect(r*w+c,r*w+c+1)
        if r*w+c-1 in s and c-1>=0:
            connect(r*w+c,r*w+c-1)
    else:
        a,b,c,d=q[1:]
        if (a*w+b in s) and (c*w+d in s) and root(a*w+b)==root(c*w+d):
            print("Yes")
        else:
            print("No")