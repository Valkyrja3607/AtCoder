n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append([int(j) for j in list(input())])
ans=[[0]*m for i in range(n)]
for i in range(1,n-1):
    for j in range(1,m-1):
        if a[i-1][j]*a[i+1][j]*a[i][j-1]*a[i][j+1]!=0:
            p=min(a[i-1][j],a[i+1][j],a[i][j-1],a[i][j+1])
            a[i-1][j]-=p
            a[i+1][j]-=p
            a[i][j-1]-=p
            a[i][j+1]-=p
            ans[i][j]+=p
for s in ans:
    l=map(str,s)
    print("".join(l))
