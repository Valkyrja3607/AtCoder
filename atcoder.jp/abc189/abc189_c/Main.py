n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    tmp=10**18
    for j in range(n-i):
        tmp=min(a[i+j],tmp)
        ans=max(ans,tmp*(j+1))
print(ans)