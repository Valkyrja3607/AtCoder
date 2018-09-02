n,k=map(int,input().split())

ans=0

if k%2==1:
    ans=int(n/k)**3
else:
    ans=int(n/k+0.5)**3+(n//k)**3
    
print(ans)