from subprocess import*
call(('pypy3','-c',"""
import sys
sys.setrecursionlimit(10**6)
h,w=map(int,input().split())
a=[[int(j) for j in input().split()] for _ in range(h)]
mod=10**9+7
ans=0
l=[[-1]*w for j in range(h)]

def f(i,j):
    if l[i][j]!=-1:
        return l[i][j]
    tmp=1
    for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
        p,q=i+x,j+y
        c=0
        if 0<=p<h and 0<=q<w:
            if a[p][q]>a[i][j]:
                tmp+=f(p,q)
                tmp%=mod
            else:
                c+=1
        else:
            c+=1
    if c==4:
        l[i][j]=1
        return 1
    else:
        l[i][j]=tmp
        return tmp

for i in range(h):
    for j in range(w):
        ans+=f(i,j)
        ans%=mod
print(ans)

"""))