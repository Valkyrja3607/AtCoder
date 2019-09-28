n=int(input())
a=[int(j) for j in input().split()]
l=[]
for i in range(n):
    l.append([a[i],i+1])
l.sort()
ans=[]
for i,j in l:
    ans.append(j)
print(*ans)