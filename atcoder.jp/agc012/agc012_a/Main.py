n=int(input())
a=[int(i) for i in input().split()]
a.sort()
a=a[::-1]
ans=0
for i in range(n):
    ans+=a[i*2+1]

print(ans)
