b=[int(j) for j in input().split()]
n=int(input())
a=[input() for i in range(n)]
l=[]
ll=[0]*10
for i in range(10):
    ll[b[i]]=i
for s in a:
    tmp=""
    for i in s:
        tmp+=str(ll[int(i)])
    l.append((int(tmp),s))
l.sort()

for i,j in l:
    print(j)






