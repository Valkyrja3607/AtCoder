a,b=[int(i) for i in input().split()]
c=abs(b-a)
ans=0
while c>10:
    c-=10
    ans+=1
if 1<=c and c<=3:
    ans+=c
elif 4<=c and c<=7:
    ans+=abs(5-c)+1
elif c>=8:
    ans+=11-c
print(ans)







