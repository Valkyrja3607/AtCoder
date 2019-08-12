r,b=map(int,input().split())
x,y=map(int,input().split())
ans=0
left=0
right=r+b
while right-left>1:
    k=(left+right)//2
    if (r-k)//(x-1)+(b-k)//(y-1)>=k and r>=k and b>=k:
        left=k
    else:
        right=k
print(left)