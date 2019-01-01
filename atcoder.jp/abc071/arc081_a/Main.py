n=int(input())
a=[int(i) for i in input().split()]

import collections
 
c=collections.Counter(a)
l=c.most_common()

from operator import itemgetter

l.sort(key=itemgetter(0))   
l.reverse()

ans=[]
for i,j in l:
    if j>=4:
        ans.append(int(i))
        ans.append(int(i))
        break
    if j>=2:
        ans.append(int(i))
        if len(ans)==2:
            break

if len(ans)<2:
    ans.append(0)
    ans.append(0)
print(ans[0]*ans[1])