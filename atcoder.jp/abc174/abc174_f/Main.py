import sys
readline = sys.stdin.readline
read = sys.stdin.read
 
n,q = [int(i) for i in readline().split()]
ll = [0]+[int(i) for i in readline().split()]
lr = [[int(i) for i in readline().split()]+[j] for j in range(q)]

size=(2*n)+1
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

lr.sort(key = lambda x: x[1])
c=[-1]*(n+1)
ans=[0]*q
idx=0
for i in range(1,n+1):
    if c[ll[i]]!=-1:
        bit_update(c[ll[i]],-1)
    c[ll[i]]=i
    bit_update(i,1)
    while idx<q and lr[idx][1]<=i:
        ans[lr[idx][2]]=bit_sum(lr[idx][1])-bit_sum(lr[idx][0]-1)
        idx+=1
print('\n'.join(map(str,ans)))