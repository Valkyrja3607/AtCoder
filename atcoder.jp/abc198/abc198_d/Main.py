import itertools
import collections
a=input()
al=collections.Counter()
for i,j in enumerate(a[::-1],0):
    if not al[j]:
        al[j]=[]
    al[j].append(10**i)
s=set(list(a))
b=input()
bl=collections.Counter()
for i,j in enumerate(b[::-1],0):
    if not bl[j]:
        bl[j]=[]
    bl[j].append(10**i)
s|=set(list(b))
c=input()
s|=set(list(c))
cl=collections.Counter()
for i,j in enumerate(c[::-1],0):
    if not cl[j]:
        cl[j]=[]
    cl[j].append(10**i)
s=list(s)
ini=set([a[0],b[0],c[0]])
if len(s)>10:
    print("UNSOLVABLE")
    exit()
cnt=0
for x in itertools.permutations(range(10),len(s)):
    cnt+=1
    p,q,r=0,0,0
    b=True
    for i,j in enumerate(x):
        if j==0 and s[i] in ini:
            b=False
        if al[s[i]]:
            for k in al[s[i]]:
                p+=k*j
        if bl[s[i]]:
            for k in bl[s[i]]:
                q+=k*j
        if cl[s[i]]:
            for k in cl[s[i]]:
                r+=k*j
    if b and p+q==r:
        print(p)
        print(q)
        print(r)
        exit()
print("UNSOLVABLE")
exit()  