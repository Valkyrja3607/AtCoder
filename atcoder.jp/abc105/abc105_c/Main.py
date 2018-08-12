n=int(input())
a=[]
k=0

if n==0:
    print(0)

while k<1:
    if n==0:
        k=1
    else:
        if n%2==0:
            a.append(0)
            n=n/(-2)
        else:
            a.append(1)
            n=(n-1)/(-2)
            
for i in (reversed(a)):
    print(i,end="")