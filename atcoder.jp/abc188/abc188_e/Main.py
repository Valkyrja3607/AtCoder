n,m=map(int,input().split())
a=list(map(int,input().split()))
g=[[]for i in range(n)]
for i in range(m):
    x,y=map(int,input().split())
    g[x-1].append(y-1)
l=[10**20]*n
ans=-10**20

for i in range(n):
    for j in g[i]:
        l[j]=min(a[i],l[i],l[j])
        ans=max(ans,a[j]-l[j])

print(ans)