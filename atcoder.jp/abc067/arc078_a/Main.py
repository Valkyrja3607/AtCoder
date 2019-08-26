n=int(input())
l=[int(i) for i in input().split()]
s=sum(l)
a=0
ans=10**100
for i in range(n-1):
    s-=l[i]
    a+=l[i]
    ans=min(ans,abs(a-s))
print(ans)





