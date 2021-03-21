n=int(input())
l=[[int(i)for i in input().split()]for j in range(n)]
s=[]
m=10**10
for i in range(n):
    m=min(l[i][0],m)
    tmp=[]
    for j,k in zip(l[i],l[i][1:]):
        tmp.append(j-k)
    s.append(tmp)
for a,b in zip(s,s[1:]):
    if a!=b:
        print("No")
        exit()
print("Yes")
s=s[0]
b=[m]
a=[]
for i in s:
    b.append(b[-1]-i)
for i in range(n):
    a.append(l[i][0]-m)
print(*a)
print(*b)