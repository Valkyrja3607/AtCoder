n=int(input())

a=[105,135,165,189,195]
ans=0

for i in a:
    if i<=n:
        ans+=1

print(ans)