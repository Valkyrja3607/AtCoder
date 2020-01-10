n,m=[int(j) for j in input().split()]
a=[int(j) for j in input().split()]
l=set()

for i in a:
    if i%2==0:
        l.add(i//2)
    else:
        print(0)
        exit()

c=1
l=list(l)
p=l[0]
while True:
    if p%2==0:
        c*=2
        p=p//2
    else:
        break

for i in l:
    if i%c!=0:
        print(0)
        exit()
    if (i//c)%2==0:
        print(0)
        exit()


def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

#最小公倍数
def lcm(x,y):
    return x*y//gcd(x,y)

p=1
for i in l:
    p=lcm(p,i)


ans=m//p
import math
print(math.ceil(ans/2))





