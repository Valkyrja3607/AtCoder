n,l=map(int,input().split())
k=int(input())
a=list(map(int,input().split()))

def f(x):
    pre=0
    cnt=0
    for i in a+[l]:
        if i-pre>=x:
            cnt+=1
            pre=i
    if cnt>=k+1:
        return True
    return False

left=0
right=l
while right-left>1:
    mid=(left+right)//2
    if f(mid):
        left=mid   #ここがleftならansもleft。
    else:
        right=mid
print(left)