n=int(input())
p=[int(j) for j in input().split()]
q=[int(j) for j in input().split()]
l=list(range(1,n+1)[::-1])
import itertools
ll=[]
for x in itertools.permutations(l):
    ll.append(list(x))
ll.sort()
a=0
b=0
c=0
for i in ll:
    if i==p:
        a=c
    if i==q:
        b=c
    c+=1
print(abs(a-b))
