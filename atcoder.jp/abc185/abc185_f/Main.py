n,q=map(int,input().split())
a=list(map(int,input().split()))

size=2*n+1
bit=[0]*size
def bit_update(x,v):
    while x<size:
        bit[x]^=v
        x+=(x&-x)
def bit_sum(n):
    s=0
    if n==0:return 0
    x=n
    while x>0:
        s^=bit[x]
        x-=(x&-x)
    return s

for i,j in enumerate(a,1):
    bit_update(i,j)

for i in range(q):
    t,x,y=map(int,input().split())
    if t==1:
        bit_update(x,y)
    else:
        print(bit_sum(y)^bit_sum(x-1))