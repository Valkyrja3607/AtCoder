n,k=map(int,input().split())
a=[int(j) for j in input().split()]
f=[int(j) for j in input().split()]
a.sort()
f.sort()
f.reverse()
if k>=sum(a):
    print(0)
    exit()

ans=[]
a.sort()
for i in range(n):
    ans.append([a[i]*f[i],a[i]])
ans.sort()
ans.reverse()

def fun(m):
    p=0
    for i,j in zip(a,f):
        if i>m//j:
            p+=i-(m//j)
            if p>k:
                return False
    return True

left=0
right=ans[0][0]
while right-left>1:
    mid=(left+right)//2
    if fun(mid):
        right=mid   #ここがleftならansもleft。
    else:
        left=mid

print(right)




