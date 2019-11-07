n=int(input())
t=[int(j) for j in input().split()]
m=int(input())
ans=[sum(t)]*m
for i in range(m):
    p,x=[int(j) for j in input().split()]
    ans[i]-=t[p-1]-x
for i in ans:
    print(i)
