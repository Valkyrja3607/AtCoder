n=int(input())
t=list(map(int,input().split()))
import collections
dp=set()
dp.add(0)
s=sum(t)
ans=10**18
for i in t:
    l=[]
    for j in dp:
        l.append(i+j)
        ans=min(ans,max(s-j-i,j+i))
    for j in l:
        dp.add(j)
print(ans)


