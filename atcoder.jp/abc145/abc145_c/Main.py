n=int(input())
xy=[]
for i in range(n):
    xy.append([int(j) for j in input().split()])
ans=0
import itertools
for l in itertools.permutations("01234567"[:n]): 
    for i in range(n-1):
        x=xy[int(l[int(i)])][0]-xy[int(l[int(i+1)])][0]
        y=xy[int(l[int(i)])][1]-xy[int(l[int(i+1)])][1]
        ans+=((x)**2+(y)**2)**0.5
import math
print(ans/(math.factorial(n)))
