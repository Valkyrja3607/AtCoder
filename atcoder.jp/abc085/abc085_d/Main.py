n,h=map(int,input().split())
ab=[]
for i in range(n):
    ab.append([int(j) for j in input().split()])

from operator import itemgetter
ab.sort(key=itemgetter(0))
nm=ab[-1][0] 

ab.sort(key=itemgetter(1)) 
ab.reverse()

ans=0
for i in range(n):
    if ab[i][1]>=nm:
        h-=ab[i][1]
        ans+=1
    if h<=0:
        print(ans)
        import sys
        sys.exit()
import math
ans+=math.ceil(h/nm)
print(ans)