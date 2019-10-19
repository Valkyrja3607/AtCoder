n=int(input())
l=[int(i) for i in input().split()]
l.sort()
ll=[0]*(l[-1]+1)

for i in l:
    ll[i]+=1
for i in range(1,len(ll)):
    ll[i]+=ll[i-1]

ans=0
import itertools
for i,j in itertools.combinations(l,2):
    if max(i-j,j-i)<i+j-1:
        ans+=ll[min(len(ll)-1,i+j-1)]-ll[min(len(ll)-1,max(i-j,j-i))]
        if max(i-j,j-i)<i<i+j:
            ans-=1
        if max(i-j,j-i)<j<i+j:
            ans-=1
print(ans//3)


