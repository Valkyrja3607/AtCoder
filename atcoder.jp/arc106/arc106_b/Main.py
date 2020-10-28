n,m=map(int,input().split())
a=[int(i)for i in input().split()]
b=[int(i)for i in input().split()]
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

for i in range(m):
    l=[int(j)-1 for j in input().split()]
    if root(l[0])!=root(l[1]):
        connect(l[0],l[1])

c=[[0,0]for i in range(n)]
for i in range(n):
    p=root(i)
    if p<-1:
        p=i
    if p==-1:
        if a[i]!=b[i]:
            print("No")
            exit()
    else:
        c[p][0]+=a[i]
        c[p][1]+=b[i]

for i,j in c:
    if i!=j:
        print("No")
        exit()
print("Yes")