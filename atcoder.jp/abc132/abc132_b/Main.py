n=int(input())
p=[int(i) for i in input().split()]
ans=0
for i in range(n-2):
    l=[p[i],p[i+1],p[i+2]]
    if p[i+1]==sum(l)-max(l)-min(l):
        ans+=1
print(ans)