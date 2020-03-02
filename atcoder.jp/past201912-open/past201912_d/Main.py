n=int(input())
a=list(int(input()) for i in range(n))
s=set(range(1,n+1))
import collections
c=collections.Counter(a)
ll=c.most_common()
p,q=s-set(a),ll[0][0]
l=0
for i in p:
    l=i
if p:
    print(q,l)
else:
    print("Correct")