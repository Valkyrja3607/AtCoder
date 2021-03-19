n=int(input())
a=list(map(int,input().split()))
import collections
c=collections.Counter(a)
ans=0
for i in c:
    tmp=0
    for j in c:
        tmp+=c[j]*(i-j)**2
    ans+=tmp*c[i]
print(ans//2)