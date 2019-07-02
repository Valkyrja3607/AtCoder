#ワ―シャルフロイド法   d=[[0,1],[2,0]]を最短コストに変換する感じ
def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

n,m=map(int,input().split())
abc=[]
d=[[10**9+7 for i in range(n)] for j in range(n)]
l=[[10**9+7 for i in range(n)] for j in range(n)]
for i in range(m):
    tmp=[int(j) for j in input().split()]
    abc.append(tmp)
    d[tmp[0]-1][tmp[1]-1]=tmp[2]
    d[tmp[1]-1][tmp[0]-1]=tmp[2]
    l[tmp[0]-1][tmp[1]-1]=tmp[2]
    l[tmp[1]-1][tmp[0]-1]=tmp[2]

for i in range(n):
    d[i][i]=0
    l[i][i]=0
d=warshall_floyd(d)

ans=0
for i in range(n):
    for j in range(n):
        if d[i][j]!=l[i][j] and l[i][j]!=10**9+7:
            ans+=1
print(ans//2)

    
    