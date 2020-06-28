import time
st=time.time()
d=int(input())
c=[0]+[int(j)for j in input().split()]
s=[[0]+[int(j)for j in input().split()]for i in range(d)]
s2=[sorted([[j,idx]for idx,j in enumerate(s[i])],reverse=True)for i in range(d)]
t=[i[0][1]for i in s2]
ans=0
p=1
q=t[0]-1
se=set()
while time.time()-st<1.8:
    if len(se)==26:
        p+=1
        if p>d:p=1
        se=set()
        q=t[p-1]
    se.add(q)
    l=[0]*27
    tmp=0
    pre=t[p-1]
    t[p-1]=q
    for i,j in enumerate(t,1):
        tmp+=s[i-1][j]
        l[j]=i
        for k in range(1,27):
            tmp-=(i-l[k])*c[k]
    if ans<tmp:
        ans=tmp
    else:
        t[p-1]=pre
    nextq=list(set(range(1,27))-se)
    if nextq!=[]:
        q=nextq[0]

for i in t:
    print(i)

