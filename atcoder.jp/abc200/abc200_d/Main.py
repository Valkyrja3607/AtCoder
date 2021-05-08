n=int(input())
a=list(map(int,input().split()))
a=[i%200 for i in a]
import collections
c=collections.Counter(a)
ll=c.most_common()
if len(ll)!=n:
    print("Yes")
    for i,j in ll:
        if j>1:
            break
    b=False
    for idx,j in enumerate(a,1):
        if j==i:
            print(1,idx)
            if b:
                exit()
            b=True
d={}
for i in range(200):
    d[i]=[]

if n>10:
    cnt=1000
else:
    cnt=2**n

for i in range(1,cnt):
    tmp=0
    l=[]
    for j in range(n):
        if i>>j&1:
            l.append(j+1)
            tmp=(tmp+a[j])%200
    if d[tmp]!=[]:
        print("Yes")
        print(len(d[tmp]),*d[tmp])
        print(len(l),*l)
        exit()
    else:
        d[tmp]=l
print("No")

            





