n,m=map(int,input().split())
ans=set()
ans.add(0)
l=[1 for i in range(n)]
for i in range(m):
    x,y=[int(j)-1 for j in input().split()]
    l[x]-=1
    l[y]+=1
    if x in ans:
        ans.add(y)
        if l[x]==0:
            ans.remove(x)
print(len(ans))