n=int(input())
l=[int(i) for i in input().split()]
l.sort()
ans=0
for i in range(2*n):
    if i%2==0:
        ans+=l[i]
print(ans)