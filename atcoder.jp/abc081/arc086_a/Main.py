import collections
n,k=map(int,input().split())
a=[int(i) for i in input().split()]

c=collections.Counter(a)
l=[]

for i,j in c.most_common():
    l.append(j)

l.sort()
l.reverse()
ans=n


for i in range(k):
    ans-=l[i]
    if ans==0:
        break
print(ans)