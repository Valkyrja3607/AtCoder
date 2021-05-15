a=list(map(int,input().split()))
a.sort()
x,y,z=a
if z-y==y-x:
    print("Yes")
else:
    print("No")