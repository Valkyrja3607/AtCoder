import sys

n=int(input())

a=0
b=0

for i in range(n):
    ti,x,y=map(int,input().split())
    s=abs(x+y-b)
    t=ti-a
    if t>=s and (s-t)%2==0:
        a=ti
        b=x+y
    else:
        print("No")
        sys.exit()
    
print("Yes")