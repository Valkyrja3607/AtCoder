n,m=map(int,input().split())
a=[]
for i in range(m):
    a.append([int(j) for j in input().split()])

table=[0]*(n+2)
for i in range(m):
    table[a[i][0]]+=1
    table[a[i][1]+1]-=1

for i in range(1,n+1):
    table[i]+=table[i-1]

ans=0
for i in table:
    if i==m:
        ans+=1

print(ans)