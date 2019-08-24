s=input()
l=list(s)
import collections
c=collections.Counter(l)
ll=c.most_common()
if len(s)==len(ll):
    print("yes")
else:
    print('no')