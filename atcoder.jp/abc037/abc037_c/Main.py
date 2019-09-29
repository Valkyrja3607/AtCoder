n,k=[int(j) for j in input().split()]
a=[int(j) for j in input().split()]
s=sum(a[:k])
ans=s
for i in range(k,n):
    s+=a[i]
    s-=a[i-k]
    ans+=s
print(ans)




