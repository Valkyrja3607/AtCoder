n,k=map(int,input().split())
l=[int(input()) for j in range(n)]
ans=sum(l[:k])
tmp=sum(l[:k])
for i in range(n-k):
    tmp+=l[i+k]-l[i]
    ans=max(tmp,ans)
print(ans)