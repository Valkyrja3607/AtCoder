n,c=map(int,input().split())
l=[]
for i in range(n):
    l.append(int(input()))

l.sort()
import bisect
ans=0
while l!=[]:
    i=l[0]
    x=c-1-i
    a=bisect.bisect_right(l,x)
    if a!=0 and a!=1:
        ans+=1
        del l[a-1]
        del l[0]
    else:
        del l[0]
        ans+=1

print(ans)