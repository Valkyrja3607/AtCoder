l,r=map(int,input().split())
ll=[]
mod=2019
if r-l+1>=2019:
    print(0)
    import sys
    sys.exit()
ans=10**100
import itertools
for i,j in itertools.combinations(range(l,r+1),2):
    ans=min(ans,(i*j)%mod)
print(ans)

