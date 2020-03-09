n=int(input())
a=[int(j) for j in input().split()]
ans=10**18
for i in range(101):
    tmp=0
    for j in a:
        tmp+=(i-j)**2
    ans=min(ans,tmp)
print(ans)
