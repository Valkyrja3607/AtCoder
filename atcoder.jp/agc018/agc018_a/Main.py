n,k=map(int,input().split())
a=[int(i) for i in input().split()]
a.sort()
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
ans=a[0]
for i in a:
    ans=gcd(ans,i)

if k%ans==0 and max(a)>=k:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")




