n,m=map(int,input().split())
a=[int(i) for i in input().split()]
bc=[]
for i in range(m):
    bc.append([int(j) for j in input().split()])

a.sort()

from operator import itemgetter
bc.sort(key=itemgetter(1))
bc.reverse()

ans=0
for i in range(n):
    if bc!=[]:
        if a[i]<bc[0][1]:
            ans+=bc[0][1]
            if bc[0][0]==1:
                 del bc[0]
            else:
                bc[0][0]-=1
        else:
            ans+=a[i]
    else:
        ans+=a[i]
print(ans)
