n=int(input())
a=[int(j)for j in input().split()]
a.sort(reverse=True)
ans=0
for i,j in enumerate(a):
    ans+=(n-i*2-1)*j
print(ans)