s=int(input())
k=int(input())

st=str(s)
l=len(st)
i=0
a=0
n=0
m=0

while n<1:
    if int(st[m])==1:
        m+=1
        a+=1
    else:
        n=1
    if a==l:
        n=1

if a>=k:
    print(1)

else:
    while i<=l:
        if int(st[i])!=1:
            print(int(st[i]))
            i=l+1
        else:
            i+=1