import sys
input=sys.stdin.readline
n,m=map(int,input().split())

#Union-Find
par=[-1 for i in range(n)]    #par<0なら自身が親で要素の個数、>0なら子で親の位置示す

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

l=[[] for i in range(n)]
for i in range(m):
    a=[int(j)-1 for j in input().split()]
    l[a[0]].append(a[1])
    l[a[1]].append(a[0])
    if root(a[0])!=root(a[1]):
        connect(a[0],a[1])

ans=0
from collections import deque
for i in range(n):
    if par[i]<0:
        ans+=1
        q=deque([(i,i)])
        b=i
        s=set()
        while q:
            p,b=q.pop()
            t=False
            for j in l[p]:
                if j==b:
                    continue
                if j in s:
                    ans-=1
                    t=True
                    break
                q.append((j,p))
            if t:
                break
            s.add(p)

print(ans)

