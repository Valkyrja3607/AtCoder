s=input()
l=list(s)
import collections
c=collections.Counter(l)
ll=c.most_common()

for i,j in ll:
    if j!=2:
        print("No")
        import sys
        sys.exit()
print("Yes")