n,x=map(int,input().split())
a=[int(j) for j in input().split()]
m=max(a)
ans=0
for i in a:
    if i+x>=m:
        ans+=1
print(ans)