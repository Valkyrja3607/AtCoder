n,m=map(int,input().split())
a=[0]+[int(j)for j in input().split()]
bb=[[int(j)for j in input().split()]for _ in range(m)]
b=[]
for l in bb:
    b.append([l[0],set(l[2:])])
import itertools
ans=0
for l in itertools.combinations(range(1,n+1),9):
    tmp=sum([a[i]for i in l])
    s=set(l)
    for i,j in b:
        if len(j&s)>=3:
            tmp+=i
    if ans<tmp:ans=tmp
print(ans)