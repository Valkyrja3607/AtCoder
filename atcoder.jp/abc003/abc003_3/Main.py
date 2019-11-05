n,k=[int(j) for j in input().split()]
a=[int(j) for j in input().split()]
a.sort()
a.reverse()
ans=0.0
for i in range(k)[::-1]:
    ans=(ans+a[i])/2
print(ans)