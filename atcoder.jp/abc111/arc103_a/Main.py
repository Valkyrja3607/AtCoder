from collections import Counter
n=int(input())
a=[int(i) for i in input().split()]

o=[]
e=[]


for i in range(n):
    if i%2==1:
        o.append(a[i])
    else:
        e.append(a[i])

oc = Counter(o)
ec = Counter(e)

ok=[]
ek=[]
ol=[]
el=[]
for word, cnt in oc.most_common():
    ok.append(cnt)
    ol.append(word)
for word, cnt in ec.most_common():
    ek.append(cnt)
    el.append(word)

if len(ok)==1:
    ok.append(0)
if len(ek)==1:
    ek.append(0)
if el[0]!=ol[0]:
    print(n-ok[0]-ek[0])
else:
    print(min(n-ok[1]-ek[0],n-ok[0]-ek[1]))
