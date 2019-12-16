n,m=[int(j) for j in input().split()]
l=set()
for i in range(m):
    x,y=[int(j) for j in input().split()]
    l.add((x,y))
ans=1
import itertools
for i in range(1,1+n):
    for x in itertools.combinations(list(range(1,13)),i):
        c=True
        for p,q in itertools.combinations(x,2):
            if p>q:
                p,q=q,p
            if not (p,q) in l:
                c=False
                break
        if c:
            ans=i
print(ans)


