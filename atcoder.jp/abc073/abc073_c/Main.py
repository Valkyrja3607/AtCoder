n=int(input())

a=[]

for i in range(n):
    n=int(input())
    a.append(n)
    
import collections
l=collections.Counter(a)


ans=0

for i,j in l.most_common():
    if j%2==1:
        ans+=1

print(ans)