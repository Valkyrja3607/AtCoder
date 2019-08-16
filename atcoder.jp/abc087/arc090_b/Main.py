#重み付きUnion-Find
#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        px = find(par[x])
        wei[x] += wei[par[x]]
        par[x] = px
        return px

#xの根から距離
def weight(x):
    find(x)
    return wei[x]


#w[y]=w[x]+wとなるようにxとyを併合
def unite(x,y,w):
    w += wei[x]-wei[y]
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
            w = -w
        par[x] += par[y]
        par[y] = x
        wei[y] = w
        return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]

#x,yが同じ集合に属するときのwei[y]-wei[x]
def diff(x,y):
    return weight(y)-weight(x)

n,m = map(int,input().split())

#初期化
#par:根なら-size,子なら親の頂点
#wei:親からの距離,根なら0
par = [-1]*(n+1)
wei = [0]*(n+1)

ans=True
for i in range(m):
    p=[int(j) for j in input().split()]
    if same(p[0],p[1]):
        if diff(p[0],p[1])!=p[2]:
            ans=False
    else:
        unite(p[0],p[1],p[2])

if ans:
    print("Yes")
else:
    print("No")