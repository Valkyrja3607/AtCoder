n=int(input())
a=[int(input())for i in range(n)]
l=[]
import bisect
for i in a:
    if l==[]:
        l.append(i)
    else:
        if l[-1]<i:
            l.append(i)
        else:
            l[bisect.bisect_left(l,i)]=i
print(n-len(l))