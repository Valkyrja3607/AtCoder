n,k=map(int,input().split())
a=[int(i) for i in input().split()]

m=40
f=[0]*m
b=False
ans=0
for i in a:
    for j in range(m):
        f[j]+=i>>j&1
for i in range(m)[::-1]:
    if f[i]>n//2:
        ans+=f[i]*2**i
        if k>>i&1:
            b=True
    else:
        if b or k>>i&1:
            ans+=(n-f[i])*2**i
        else:
            ans+=f[i]*2**i
print(ans)