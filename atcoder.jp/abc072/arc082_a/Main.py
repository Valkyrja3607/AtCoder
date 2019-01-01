n=int(input())
a=[int(i) for i in input().split()]

import collections
 
c=collections.Counter(a)
l=c.most_common()

from operator import itemgetter

l.sort(key=itemgetter(0))   
    

ans=0
for i in range(len(l)-2):
    if int(l[i][0])+1==int(l[i+1][0]) and int(l[i+1][0])+1==int(l[i+2][0]):
        ans=max(ans,l[i][1]+l[i+1][1]+l[i+2][1])
    elif int(l[i][0]+1)==int(l[i+1][0]):
        ans=max(ans,l[i][1]+l[i+1][1])
    else:
        ans=max(ans,l[i][1])

if len(l)==1:
    ans=l[0][1]

if len(l)==2:
    if int(l[1][0])-int(l[0][0])<=2:
        ans=l[0][1]+l[1][1]
    else:
        ans=max(ans,l[0][1],l[1][1])
        
print(ans)




