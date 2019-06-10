def eratosthenes(n):
    table = [0] * (n + 1)
    prime_list = []
    
    for i in range(2, n + 1):
        if table[i] == 0:
            prime_list.append(i)
            for j in range(i + i, n + 1, i):
                table[j] = 1
                
    return prime_list

lr=[]
q=int(input())
p=0
for i in range(q):
    a=[int(j) for j in input().split()]
    lr.append(a)
    p=max(p,a[1])
ll=eratosthenes(p)
l=set(ll)
del ll[0]
li=[0 for i in range(p+2)]

for i in ll:
    if (i+1)//2 in l:
        li[i]+=1

from itertools import accumulate
la=list(accumulate(li))

for i in range(len(lr)):
    print(la[lr[i][1]]-la[lr[i][0]-1])



