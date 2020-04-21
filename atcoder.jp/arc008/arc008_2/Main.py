n,m=map(int,input().split())
s=input()
k=input()
import collections
cs=collections.Counter(s)
ck=collections.Counter(k)
ans=0
for i in cs:
    if ck[i]==0:
        print(-1)
        exit()
    if -(-cs[i]//ck[i])>ans:
        ans=-(-cs[i]//ck[i])
print(ans)