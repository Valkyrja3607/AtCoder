n,x=[int(j) for j in input().split()]
m=[]
for i in range(n):
    m.append(int(input()))
ans=n
x-=sum(m)
ans+=x//min(m)
print(ans)





