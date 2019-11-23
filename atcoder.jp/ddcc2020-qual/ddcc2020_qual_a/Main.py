x,y=[int(j) for j in input().split()]
if x==1 and y==1:
    print(1000000)
    exit()
ans=0
if x==1:
    ans+=300000
elif x==2:
    ans+=200000
elif x==3:
    ans+=100000
if y==1:
    ans+=300000
elif y==2:
    ans+=200000
elif y==3:
    ans+=100000
print(ans)