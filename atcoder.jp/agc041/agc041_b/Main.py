n,m,v,p=[int(j) for j in input().split()]
a=[int(j) for j in input().split()]
a.sort(reverse=True)

def f(x):
    if x>n-1:
        return False
    if x<p:
        return True
    if a[x]+m<a[p-1]:
        return False
    tmp=m*(p+n-x-1)
    for i in range(p-1,x):
        tmp+=a[x]+m-a[i]
    if tmp>=m*v:
        return True
    return False

left=0
right=n
while right-left>1:
    mid=(left+right)//2
    if f(mid):
        left=mid
    else:
        right=mid
print(left+1)

