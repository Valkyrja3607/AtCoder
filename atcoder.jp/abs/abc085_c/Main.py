N,Y=map(int,input().split())

a=0
b=0
c=0

for x in range(N+1):
    for y in range(N-x+1):
        if 9000*x+4000*y+1000*N==Y:
            a=x
            b=y
            c=N-x-y
            
if a==0 and b==0 and c==0:
    a=-1
    b=-1
    c=-1
    
print(str(a)+" "+str(b)+" "+str(c))