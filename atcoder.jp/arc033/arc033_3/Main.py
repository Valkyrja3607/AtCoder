size=(1<<18)+1
bit=[0]*size
def bit_update(x,v):
    while x<size:
        bit[x]+=v
        x+=(x&-x)
def bit_sum(n):
    s=0
    if n==0:return 0
    x=n
    while x>0:
        s+=bit[x]
        x-=(x&-x)
    return s

def lower_bound(v):
    x,sx=0,0
    step=size-1
    while step:
        y=x+step
        sy=sx+bit[y]
        if sy<v:
            x,sx=y,sy
        step>>=1
    return x+1

import sys
input=sys.stdin.readline
q=int(input())
for _ in range(q):
    t,x=map(int,input().split())
    if t==1:
        bit_update(x,1)
    else:
        a=lower_bound(x)
        print(a)
        bit_update(a,-1)