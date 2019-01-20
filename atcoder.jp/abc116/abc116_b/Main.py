s=int(input())

a=[s]
k=0
ans=2
while k==0:
    if a[-1]%2==0:
        p=a[-1]//2
    else:
        p=3*a[-1]+1
    for i in a:
        if i==p:
            print(ans)
            k=1
            break
    a.append(p)
    ans+=1


