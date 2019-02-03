n,m=map(int,input().split())
x=[int(i) for i in input().split()]
x.sort()

if n>=m:
    print(0)
    import sys
    sys.exit()
l=[]
ans=x[-1]-x[0]
for i in range(m-1):
    l.append(abs(x[i]-x[i+1]))
l.sort()
l.reverse()
for i in range(n-1):
    ans-=l[i]
if ans>=0:
    print(ans)
else:
    print(0)