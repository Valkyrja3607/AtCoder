n=int(input())
s=input()
from collections import Counter
l=Counter()
l["R"]=[]
l["G"]=[]
l["B"]=[]
for j,i in enumerate(s):
    if l[i]==0:
        l[i]=[]
    l[i].append(j)
ans=0
import bisect
import itertools
ll=Counter()
ll["R"]=len(l["R"])
ll["G"]=len(l["G"])
ll["B"]=len(l["B"])
for i,j in itertools.combinations(range(n),2):
    if s[i]!=s[j]:
        c="RGB".replace(s[i],"").replace(s[j],"")
        idx=bisect.bisect_left(l[c],j)
        ans+=ll[c]-idx
        if 2*j-i<n:
            if s[2*j-i]==c:
                ans-=1
print(ans)


