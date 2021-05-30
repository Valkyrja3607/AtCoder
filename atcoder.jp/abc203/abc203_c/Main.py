n,k=map(int,input().split())
l=[list(map(int,input().split()))for i in range(n)]
l.sort()
m=k
for i,j in l:
    if i<=m:
        m+=j
    else:
        break
print(m)