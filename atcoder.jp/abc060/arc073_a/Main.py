n,T=map(int,input().split())
t=[int(i) for i in input().split()]

ans=0
s=0
for i in range(n):
    if i>0:
        if t[i]-t[i-1]>=T:
            ans+=T
        else:
            ans+=t[i]-t[i-1]
            
print(ans+T)
