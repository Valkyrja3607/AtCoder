s=input()
from itertools import*
ans=""
for k,v in groupby(s):
    ans+=k+str(len(list(v)))
print(ans)