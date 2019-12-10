n=int(input())
m=int(n**0.5)+1
ans=10**18
for i in range(1,m+1):
    for j in range(1,n//i+1):
        if n>=i*j:
            ans=min(ans,abs(i-j)+n-i*j)
print(ans)