n,k=map(int,input().split())
ans=0
if k==0:
    print(n**2)
    import sys
    sys.exit()
    
for b in range(k,n+1):
    r=n//b
    ans+=(b-k)*r
    ans+=max(0,n%b-k+1)

print(ans)