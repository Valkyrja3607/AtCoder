n=int(input())
l=[[]for i in range(n)]
ans=set()
ll=[set() for i in range(n)]
c=1
ab=[]
from collections import Counter
ans2=Counter()
for i in range(n-1):
    a,b=[int(j)-1 for j in input().split()]
    ab.append((a,b))
    l[a].append(b)
    #l[b].append(a)

for i in range(n):
    c=1
    for j in l[i]:
        while True:
            if (c not in ll[j]) and (c not in ll[i]):
                ll[j].add(c)
                ll[i].add(c)
                ans.add(c)
                ans2[(i,j)]=c
                break
            else:
                c+=1
print(len(ans))
#print(ans)
#print(ans2)
for i,j in ab:
    print(ans2[(i,j)])




