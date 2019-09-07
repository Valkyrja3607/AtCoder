n=int(input())
a=[int(j)-1 for j in input().split()]
b=[int(j) for j in input().split()]
c=[int(j) for j in input().split()]
ans=sum(b)
for i in range(1,n):
    if a[i-1]+1==a[i]:
        ans+=c[a[i-1]]
print(ans)