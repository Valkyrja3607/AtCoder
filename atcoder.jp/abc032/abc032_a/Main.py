a=int(input())
b=int(input())
n=int(input())
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
def lcm(x,y):
    return x*y//gcd(x,y)
m=lcm(a,b)
import math
k=math.ceil(n/m)
print(m*k)