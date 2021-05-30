n,k=map(int,input().split())
ans=0
for i in range(1,k+1):
    for j in range(1,n+1):
        ans+=j*100+i
print(ans)