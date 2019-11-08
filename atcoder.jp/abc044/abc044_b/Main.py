w=list(input())

import collections
c=collections.Counter(w)
l=c.most_common()
for i,j in l:
    if j%2!=0:
        print("No")
        exit()
print("Yes")