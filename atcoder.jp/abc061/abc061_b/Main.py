n,m=map(int,input().split())
ans=[0 for i in range(n+1)]
for i in range(m):
    a,b=[int(j) for j in input().split()]
    ans[a]+=1
    ans[b]+=1
for i in range(1,1+n):
    print(ans[i])
    
