n=int(input())
p=[int(j) for j in input().split()]
t=10**18
ans=0
for i in p:
    if i<=t:
        ans+=1
        t=i
print(ans)
