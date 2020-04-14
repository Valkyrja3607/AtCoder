n=int(input())
ans=0
from itertools import*
pre=n
b=True
for j in range(n):
    s=input()
    for i in range(pre)[::-1]:
        if s[i]==".":
            pre=i
            ans+=1
            b=False
            break
    if b:
        pre=n
    b=True
print(ans)