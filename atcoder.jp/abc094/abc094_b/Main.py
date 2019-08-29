n,m,x=map(int,input().split())
a=[int(i) for i in input().split()]
a=set(a)
ans=10**100
tmp=0
for i in range(x+1):
    if i in a:
        tmp+=1
ans=min(ans,tmp)
tmp=0
for i in range(x,n+1):
    if i in a:
        tmp+=1
ans=min(ans,tmp)
print(ans)