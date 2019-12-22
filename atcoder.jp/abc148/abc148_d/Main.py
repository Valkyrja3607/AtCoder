n=int(input())
a=[int(j) for j in input().split()]
ans=0
tmp=1
for i in a:
    if i==tmp:
        tmp+=1
    else:
        ans+=1

if ans==n:
    print(-1)
else:
    print(ans)