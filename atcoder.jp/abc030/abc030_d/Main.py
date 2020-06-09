n,a=map(int,input().split())
k=int(input())
b=[int(i)for i in input().split()]

s=set([a])
l=[a]
t=a
while True:
    t=b[t-1]
    if t in s:
        break
    l.append(t)
    s.add(t)

ll=[]
lr=[]
for i,j in enumerate(l):
    if j==t:
        ll=l[:i]
        lr=l[i:]
n,m=len(ll),len(lr)
if k<=n:
    print(b[ll[k-1]-1])
else:
    k-=n
    print(b[lr[(k-1)%m]-1])