n=int(input())
c=[int(input())for _ in range(n)]
from itertools import*
g=[[k,len(list(v))]for k,v in groupby(c)]
if g[0][0]==g[-1][0]:
    g[0][1]+=g[-1][1]
    del g[-1]
if len(g)==0:
    print(-1)
    exit()
ans=-(-max([j for i,j in g])//2)
print(ans)