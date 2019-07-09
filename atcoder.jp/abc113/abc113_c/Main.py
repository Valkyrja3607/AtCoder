n,m=map(int,input().split())
py=[]
for i in range(m):
    q=[int(j) for j in input().split()]
    py.append(q+[i])
from operator import itemgetter
py.sort(key=itemgetter(1))
py.sort(key=itemgetter(0))
ans=[]
q=0
c=2
for i,j,k in py:
    p=str(i).rjust(6,'0')
    if q==i:
        y=str(c).rjust(6,'0')
        c+=1
    else:
        y="000001"
        q=i
        c=2   
    ans.append([p+y,k])
from operator import itemgetter
ans.sort(key=itemgetter(1))
for i,j in ans:
    print(i)





