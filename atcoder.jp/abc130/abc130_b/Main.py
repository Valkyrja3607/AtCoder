n,x=map(int,input().split())
l=[int(j) for j in input().split()]
d=0
ans=1
for i in range(1,n+1):
    d=d+l[i-1]
    if d<=x:
        ans+=1
    else:
        break
print(ans)