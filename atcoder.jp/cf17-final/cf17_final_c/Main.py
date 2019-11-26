n=int(input())
d=[int(j) for j in input().split()]
d.sort()
d=[0]+[j if i&1 else 24-j for i,j in enumerate(d,1)]
d.sort()
ans=min(j-i for i,j in zip(d,d[1:]))
print(ans)