n=int(input())
a=[int(j) for j in input().split()]
ans=0
l=list(range(n+2))
r=list(range(n+2))

index=[0]*(n+1)
for i in range(n):
    index[a[i]]=i

for i in range(1,n+1)[::-1]:
    ind=index[i]
    x,y=l[ind],r[ind]
    ans+=i*(ind-x+1)*(y-ind+1)
    l[y+1],r[x-1]=x,y
print(ans)




