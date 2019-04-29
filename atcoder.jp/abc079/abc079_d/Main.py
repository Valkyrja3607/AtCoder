h,w=map(int,input().split())
c=[]
for i in range(10):
    c.append([int(j) for j in input().split()])
a=[]
for i in range(h):
    a.append([int(j) for j in input().split()])


n=10
def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

d=warshall_floyd(c)
ans=0

for i in range(h):
    for j in a[i]:
        if j!=-1:
            ans+=d[j][1]

print(ans)