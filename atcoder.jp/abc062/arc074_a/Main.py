h,w=map(int,input().split())
ans=10**100

for i in range(1,h):
    if w%2==0:
        l=[i*w,(h-i)*(w//2),(h-i)*(w//2)]
    else:
        l=[i*w,(h-i)*(w//2),(h-i)*(w//2+1)]

    if (h-i)%2==0:
        ll=[i*w,((h-i)//2)*w,((h-i)//2)*w]
    else:
        ll=[i*w,((h-i)//2)*w,((h-i)//2+1)*w]
    p=min(max(l)-min(l),max(ll)-min(ll))
    ans=min(ans,p)
for i in range(1,w):
    if h%2==0:
        l=[i*h,(w-i)*(h//2),(w-i)*(h//2)]
    else:
        l=[i*h,(w-i)*(h//2),(w-i)*(h//2+1)]

    if (w-i)%2==0:
        ll=[i*h,((w-i)//2)*h,((w-i)//2)*h]
    else:
        ll=[i*h,((w-i)//2)*h,((w-i)//2+1)*h]
    p=min(max(l)-min(l),max(ll)-min(ll))
    ans=min(ans,p)
print(ans)





