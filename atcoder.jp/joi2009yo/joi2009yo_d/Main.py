n=int(input())
m=int(input())
b=[[int(j) for j in input().split()] for i in range(n)]

def f(i,j,s):
    tmp=0
    l=s.copy()
    l.add((i,j))
    if b[i][j]==0:
        return 0
    if i>0 and not (i-1,j) in s:
        tmp=max(tmp,f(i-1,j,l))
    if i<m-1 and not (i+1,j) in s:
        tmp=max(tmp,f(i+1,j,l))
    if j>0 and not (i,j-1) in s:
        tmp=max(tmp,f(i,j-1,l))
    if j<n-1 and not (i,j+1) in s:
        tmp=max(tmp,f(i,j+1,l))
    return tmp+1
ans=0
for i in range(m):
    for j in range(n):
        tmp=f(i,j,set())
        if tmp>ans:
            ans=tmp
print(ans)




