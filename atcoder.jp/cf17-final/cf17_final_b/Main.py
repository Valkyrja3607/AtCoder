s=input()
l=list(s)
import collections
c=collections.Counter(l)
m=c.most_common()
ll=[]
for i,j in m:
    ll.append(j)
if len(m)<=2:
    if len(m)==1 and max(ll)==1:
        print("YES")
    elif len(m)==2 and max(ll)==1:
        print("YES")
    else:
        print("NO")
else:
    if max(ll)-min(ll)<=1:
        print("YES")
    else:
        print("NO")
