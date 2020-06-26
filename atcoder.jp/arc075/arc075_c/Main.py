n,k=map(int,input().split())
a=[int(input())for i in range(n)]
from itertools import accumulate
l=[0]+list(accumulate(a))
l=[j-k*i for i,j in enumerate(l)]

#座圧
a_to_i={a:i for i,a in enumerate(sorted(set(l)),1)}
b=[a_to_i[a]for a in l]

size=len(a_to_i)+2
bit=[0]*size

#x(index)の値にvを足す
#indexは1スタート
def bit_update(x,v):
    while x<size:
        bit[x]+=v
        x+=(x&-x) #区間の長さ

#bit_1 + bit_2 + … + bit_nをO(log(n))で求める
def bit_sum(n):
    s=0
    if n==0:return 0
    x=n
    while x>0:
        s+=bit[x]
        x-=(x&-x)
    return s

ans=0
for i in b:
    ans+=bit_sum(i)
    bit_update(i,1)
print(ans)