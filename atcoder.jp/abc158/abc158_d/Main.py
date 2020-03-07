s=input()
q=int(input())
cn=0
l1=""
l2=""
for i in range(q):
    p=input()
    if p=="1":
        cn+=1
    else:
        _,f,c=p.split()
        if f=="1":
            if cn%2==0:
                l1+=c
            else:
                l2+=c
        else:
            if cn%2==1:
                l1+=c
            else:
                l2+=c
if cn%2==1:
    s=s[::-1]
    l1,l2=l2,l1
print(l1[::-1]+s+l2)