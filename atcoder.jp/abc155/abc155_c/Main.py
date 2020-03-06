n=int(input())
l=[input() for i in range(n)]
import collections
c=collections.Counter(l)
ll=c.most_common()
tmp=ll[0][1]
ans=[]
for i,j in ll:
    if tmp==j:
        ans.append(i)
    else:
        break
ans.sort()
print('\n'.join(map(str,ans)))
