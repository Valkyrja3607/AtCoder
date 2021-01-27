def f(a):
    if a==0:
        return 1
    p=bin(a)[2:].count("1")
    return f(a%p)+1

n=int(input())
s=input()
m=s.count("1")
a,b=m-1,m+1

aa=1
bb=1
la=[]
lb=[]
if a!=0:
    aa=(aa)%a
bb=(bb)%b
la.append(aa)
lb.append(bb)
for i in range(1,n):
    if a!=0:
        aa=(2*aa)%a
    bb=(2*bb)%b
    la.append(aa)
    lb.append(bb)

sa=0
sb=0
for i,j in enumerate(s[::-1]):
    if j=="1":
        if a!=0:
            sa=(sa+la[i])%a
        sb=(sb+lb[i])%b

for i,j in enumerate(s,1):
    if j=="1":
        if a!=0:
            print(f((sa-la[-i])%a))
        else:
            print(0)
    else:
        print(f((sb+lb[-i])%b))
