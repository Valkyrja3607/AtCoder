n=int(input())
l=[]
import itertools
for i in range(3,10):
    for x in itertools.product("357",repeat=i):
        p=""
        if x.count("7")*x.count("5")*x.count("3")==0:
            continue
        for j in x:
            p+=j
        l.append(int(p))
l.sort()

import bisect
ans=bisect.bisect_right(l,n) 
print(ans)



