n=int(input())
ans=0
v=0
for i in range(2,n+1):
    print("? 1",i)
    t=int(input())
    if ans<t:
        v=i
        ans=t

for i in range(1,n+1):
    if i==v:continue
    print("?",v,i)
    ans=max(ans,int(input()))
print("!",ans)