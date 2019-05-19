n,k=map(int,input().split())
ans=0

for i in range(1,n+1):
    p=0
    while i*2**p<k:
        p+=1
    ans+=(0.5**p)/n

print(ans)