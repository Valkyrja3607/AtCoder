A,B,m=map(int,input().split())
a=[int(j) for j in input().split()]
b=[int(j) for j in input().split()]

ans=min(a)+min(b)
for i in range(m):
    x,y,c=[int(j) for j in input().split()]
    ans=min(ans,a[x-1]+b[y-1]-c)

print(ans)

