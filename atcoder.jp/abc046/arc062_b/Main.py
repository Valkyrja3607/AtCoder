s=input()
t=0
ans=0
for i in s:
    if i=="g":
        if t==0:
            t+=1
        else:
            t-=1
            ans+=1
    else:
        if t==0:
            t+=1
            ans-=1
        else:
            t-=1
print(ans)





