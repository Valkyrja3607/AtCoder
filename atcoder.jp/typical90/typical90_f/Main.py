n,k=map(int,input().split())
s=input()
c={chr(i):[] for i in range(97,123)}
d=[{chr(i):0 for i in range(97,123)}for _ in range(n)]
for i,j in enumerate(s):
    c[j].append(i)
for i in range(97,123):
    i=chr(i)
    c[i].append(1000001)
    tmp=0
    for j in range(n):
        if j>c[i][tmp]:
            tmp+=1
        d[j][i]=c[i][tmp]

ans=""
cnt=0
i=0
while i<n and cnt<k:
    for j in range(97,123):
        j=chr(j)
        if d[i][j]<=n-k+cnt:
            ans+=j
            cnt+=1
            i=d[i][j]+1
            break
print(ans)



