n=int(input())
a=[int(j) for j in input().split()]
ans=len(set(a))
if (n-ans)%2==0:
    print(ans)
else:
    print(ans-1)
