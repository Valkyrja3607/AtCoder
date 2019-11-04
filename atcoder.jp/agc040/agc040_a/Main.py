s=input()
from itertools import*
g=[[k,len(list(v))] for k,v in groupby(s)]
ans=0
for i,j in g:
    ans+=j*(j+1)//2
for i in range(len(g)-1):
    if g[i][0]=="<":
        ans-=min(g[i][1],g[i+1][1])
print(ans)