n,k=[int(j)for j in input().split()]
a=[int(j)for j in input().split()]
if n<=k:
    print(*[n]*n)
    exit()
import copy
for idx in range(k):
    table=[0]*n
    for i in range(n):
        table[max(i-a[i],0)]+=1
        if i+a[i]+1<n:
            table[i+a[i]+1]-=1
    for i in range(1,n):
        table[i]+=table[i-1]
    a=copy.deepcopy(table)
    if a==[n]*n:
        break
print(*a)