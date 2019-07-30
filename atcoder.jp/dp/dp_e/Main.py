n,W=map(int,input().split())
wv=[]
m=1
for i in range(n):
    p=[int(j) for j in input().split()]
    wv.append(p)
    m+=p[1]

dp=[10**100 for i in range(m)]
dp[0]=0

for i in range(n):
    w,v=wv[i][0],wv[i][1]
    for j in range(m):
        if dp[-1-j]!=10**100:
            dp[-1-j+v]=min(dp[-1-j+v],dp[-1-j]+w)

ans=0
for i in range(m):
    if dp[i]<=W:
        ans=i
print(ans)