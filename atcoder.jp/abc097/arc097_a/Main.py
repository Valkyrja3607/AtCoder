s=input()
k=int(input())

l=list(s)

import collections
c=collections.Counter(l)
li=c.most_common()
from operator import itemgetter
li.sort(key=itemgetter(0))

co=0
p=[]
for i in range(min(5,len(li))):
    for j in range(len(s)):
        if l[j]==li[i][0]:
            for e in range(min(len(s)-j,k)):
                co+=1
                p.append(s[j:j+e+1])

q=collections.Counter(p)
ans=q.most_common()
ans.sort(key=itemgetter(0))   

print(ans[k-1][0])      
            
            
            
            


