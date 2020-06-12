import collections
a=input()
n=len(a)//2
a=collections.Counter(a)
b=collections.Counter(input())
c=collections.Counter(input())
l=[]
s,t=0,0
for i in c:
    x,y,z=a[i],b[i],c[i]
    if x+y<z:
        print("NO")
        exit()
    s+=max(0,z-y)
    t+=min(x,z)
if s<=n<=t:
    print("YES")
else:
    print("NO")