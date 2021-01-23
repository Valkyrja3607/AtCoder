n,x=map(int,input().split())
ans=-1
tmp=0
for i in range(n):
    v,p=map(int,input().split())
    tmp+=v*p
    if tmp>x*100:
        ans=i+1
        break
print(ans)