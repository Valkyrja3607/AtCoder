n=int(input())
a=[]
b=[]
for i in range(n):
    p=[int(j) for j in input().split()]
    a.append(p[0])
    b.append(p[1])

a.reverse()
b.reverse()
ans=0
import math
for i in range(n):
    a[i]+=ans
    ans+=b[i]*math.ceil(a[i]/b[i])-a[i]
print(ans)
        


