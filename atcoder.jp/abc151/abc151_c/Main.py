n,m=map(int,input().split())
ac=set()
from collections import Counter
w=Counter()
wa=0
for i in range(m):
    p,s=input().split()
    if s=="AC":
        if p not in ac:
            wa+=w[p]
        ac.add(p)
    else:
        if p not in ac:
            w[p]+=1
print(len(ac),wa)