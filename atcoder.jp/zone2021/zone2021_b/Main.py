n,d,h=map(int,input().split())
dh=[list(map(int,input().split()))for _ in range(n)]
left=0
right=h
def f(n):
    for i,j in dh:
        if (h-n)/d*i+n<j:
            return False
    return True

while right-left>0.0005:
    mid=(left+right)/2
    if f(mid):
        right=mid   #ここがleftならansもleft。
    else:
        left=mid
print(right)