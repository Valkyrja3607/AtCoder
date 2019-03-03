a,b,q=map(int,input().split())
s=[]
t=[]
x=[]        

import bisect  

for i in range(a):
    p=int(input())
    s.append(p)
for i in range(b):
    p=int(input())
    t.append(p)
s=[-100000000000000000]+s+[1000000000000000000]
t=[-100000000000000000]+t+[1000000000000000000]
for i in range(q):
    p=int(input())
    n=bisect.bisect_right(s,p)
    m=bisect.bisect_right(t,p)
    l=[p,s[n-1],s[n],t[m-1],t[m]]
    x.append(l)

for i in range(q):
    ans=1000000000000000
    for S in [x[i][1],x[i][2]]:
        for T in [x[i][3],x[i][4]]:
            d1=abs(S-x[i][0])+abs(T-S)
            d2=abs(T-x[i][0])+abs(S-T)
            ans=min(ans,d1,d2)
    print(ans)

    

    




