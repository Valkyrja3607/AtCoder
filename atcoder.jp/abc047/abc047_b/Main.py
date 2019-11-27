w,h,n=[int(j) for j in input().split()]
xl,xr=0,w
yl,yr=0,h
for i in range(n):
    x,y,a=[int(j) for j in input().split()]
    if a==1:
        xl=max(xl,x)
    elif a==2:
        xr=min(xr,x)
    elif a==3:
        yl=max(yl,y)
    else:
        yr=min(yr,y)
if (xr-xl)>=0 and (yr-yl)>=0:
    ans=(xr-xl)*(yr-yl)
else:
    ans=0
print(ans)