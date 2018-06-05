N=int(input())
i=0

for n in range(N):
    t,x,y=map(int,input().split())
    if t<x+y or t%2 !=(x+y)%2:
        print("No")
        break
    else:
        i += 1
        
if i==N:
    print("Yes")