a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
l=[]
for i in [a,b,c,d,e]:
    l.append([(10-i%10)%10,i])

l.sort()
ans=0

for i in range(5):
    if i<=3:
        ans+=l[i][0]+l[i][1]
    else:
        ans+=l[i][1]

print(ans)
