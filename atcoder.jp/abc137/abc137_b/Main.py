k,x=map(int,input().split())
p=x-k+1
for i in range(2*k-1):
    if i!=2*k-2:
        print(p,end=" ")
    else:
        print(p)
    p+=1

