n=int(input())
l=[[int(j) for j in input().split()] for i in range(n)]
ans=0
import itertools
for ll in itertools.combinations(l,3):
    a,b,c=ll
    x1,y1=a[0]-c[0],a[1]-c[1]
    x2,y2=b[0]-c[0],b[1]-c[1]
    if abs(x1*y2-x2*y1)%2==0:
        if x1*y2-x2*y1!=0:
            ans+=1

print(ans)





