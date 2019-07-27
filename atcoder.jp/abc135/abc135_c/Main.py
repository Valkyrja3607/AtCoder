n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
ans=0
for i in range(n):
    p=min(a[i],b[i])
    a[i]-=p
    ans+=p
    q=min(b[i]-p,a[i+1])
    a[i+1]-=q
    ans+=q
print(ans)
