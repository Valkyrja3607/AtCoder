s=input()
n=len(s)
import math
m=math.ceil(n/2)
ans=0
for i in range(m):
    if s[i]!=s[n-1-i]:
        ans+=1
print(ans)