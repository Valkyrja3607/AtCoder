n,m=[int(j) for j in input().split()]
pab=[[float(j) for j in input().split()] for i in range(m)]
ll=[]
for p,a,b in pab:
    ll.append(p)
ll.sort()
from collections import Counter
l=Counter()
for i in range(m):
    l[ll[i]]=i
#A[k]をxに変更 O(logN)
def update(k,x,y):
    k += num
    seg_min[k] = x
    seg_max[k] = y
    while k>1:
        k //= 2
        seg_min[k] = seg_min[k*2]*seg_min[k*2+1]
        seg_max[k] = seg_max[k*2]*seg_min[k*2+1]+seg_max[k*2+1]

num=2**(m-1).bit_length()
seg_min=[1]*2*num
seg_max=[0]*2*num

ans1=1
ans2=1
for p,a,b in pab:
    update(l[p],a,b)
    t=seg_min[1]+seg_max[1]
    ans1=min(ans1,t)
    ans2=max(ans2,t)

print(ans1)
print(ans2)

