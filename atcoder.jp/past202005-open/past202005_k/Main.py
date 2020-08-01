import sys
sys.setrecursionlimit(10**6)
n,q=map(int,input().split())
m=2*10**5+10
l=[[m+i,-1]for i in range(1+n+m)]
ll=[[i,i]for i in range(1+n+m)]
for _ in range(q):
    f,t,x=map(int,input().split())
    y=ll[t][1]
    ll[t][1]=ll[f][1]
    ll[f][1]=l[x][0]
    l[x][0]=y
    l[y][1]=x
ans=[0]*(1+n)
def f(a):
    if ans[a]>0:
        return ans[a]
    if l[a][0]>m:
        ans[a]=l[a][0]-m
        return l[a][0]-m
    res=f(l[a][0])
    ans[a]=res
    return res
for i in range(1,1+n):
    if ans[i]==0:
        f(i)

print('\n'.join(map(str,ans[1:])))