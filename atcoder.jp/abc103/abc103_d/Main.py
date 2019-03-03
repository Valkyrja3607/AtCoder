n,m=map(int,input().split())

ab=[]

for i in range(m):
    a=[int(j) for j in input().split()]
    ab.append(a)

from operator import itemgetter
ab.sort(key=itemgetter(1))

ans=1
b=[ab[0][1]-1]
for i in range(m):
    if not b[-1]>=ab[i][0] and b[-1]<ab[i][1]:
        b.append(ab[i][1]-1)
        ans+=1

print(ans)