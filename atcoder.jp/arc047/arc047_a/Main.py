n,l=map(int,input().split())
s=input()
t=1
ans=0
for i in s:
    if i=="+":
        t+=1
    else:
        t-=1
    if t>l:
        t=1
        ans+=1
print(ans)