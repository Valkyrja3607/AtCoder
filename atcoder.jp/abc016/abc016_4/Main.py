ax,ay,bx,by=map(int,input().split())
n=int(input())
xy=[]
ans=0

a=[ax,ay]
b=[bx,by]

for i in range(n):
    xy.append([int(j) for j in input().split()])

import numpy as np
def judge(a,b,c,d):
    p1=np.array(a)
    p2=np.array(b)
    p3=np.array(c)
    p4=np.array(d)
    t1 = (p1[0] - p2[0]) * (p3[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p3[0])
    t2 = (p1[0] - p2[0]) * (p4[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p4[0])
    t3 = (p3[0] - p4[0]) * (p1[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p1[0])
    t4 = (p3[0] - p4[0]) * (p2[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p2[0])
    return t1*t2<0 and t3*t4<0

for i in range(n):
    if judge(a,b,xy[i],xy[i-1]):
        ans+=1

print((ans+2)//2)