s=input()
n=len(s)
ans=""
import math
for i in range(1,n):
    if i%2==1:
        continue
    ss=s[:i]
    m=len(ss)
    p=0
    for j in range(m//2):
        if ss[j]!=ss[j+m//2]:
            p=1
            break
    if p==0:
        ans=ss
print(len(ans))



