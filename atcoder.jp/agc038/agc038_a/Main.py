h,w,a,b=[int(j) for j in input().split()]
ans=[]
for i in range(h-b):
    print("1"*a+"0"*(w-a))
for i in range(b):
    print("0"*a+"1"*(w-a))