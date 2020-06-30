s=input().replace("25","A")
from itertools import*
g=[[k,len(list(v))]for k,v in groupby(s)]
ans=0
for i,j in g:
    if i=="A":
        ans+=j*(j+1)//2
print(ans)