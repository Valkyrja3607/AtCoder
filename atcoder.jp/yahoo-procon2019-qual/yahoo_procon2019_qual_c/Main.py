k,a,b=map(int,input().split())
import sys
if k<=a:
    print(k+1)
    sys.exit()
ans=a
k-=a-1
if k%2==1:
    k-=1
    ans+=1

if b-a>=2:
    ans+=(b-a)*(k//2)
else:
    ans+=k

print(ans)
    