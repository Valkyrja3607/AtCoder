n=int(input())
s=[input() for i in range(n)]
m=int(input())
t=[input() for i in range(m)]
ans=0
for i in s:
    ans=max(ans,s.count(i)-t.count(i))
print(ans)
