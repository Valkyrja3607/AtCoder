n,k=map(int,input().split())
a=[int(j) for j in input().split()]
a.sort(reverse=True)
def f(x):
    c=0
    for i in a:
        if i<x:
            break
        c+=-(-i//x)-1
        if c>k:
            return False
    return True
left=0
right=a[0]
while right-left>1:
    mid=(left+right)//2
    if f(mid):
        right=mid
    else:
        left=mid
print(right)