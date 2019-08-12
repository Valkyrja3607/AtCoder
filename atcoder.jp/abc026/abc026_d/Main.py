a,b,c=map(int,input().split())
import math
def f(t):
    return a*t+b*math.sin(c*t*math.pi)

left=0
right=10**15

while abs(100-f(left))>10**(-6):
    mid=(left+right)/2
    if f(mid)<=100:
        left=mid
    else:
        right=mid
print(left)