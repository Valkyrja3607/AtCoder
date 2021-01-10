n=int(input())
l=[[0,0]]
tree=[[]for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    l.append([a,b])
    tree[a].append(b)
    tree[b].append(a)
d=[-1]*(n+1)
d[1]=0
q=[1]
while q:
    i=q.pop()
    for j in tree[i]:
        if d[j]==-1:
            d[j]=d[i]+1
            q.append(j)

ans=[0]*(n+1)
z=0
q=int(input())
for i in range(q):
    t,e,x=map(int,input().split())
    a,b=l[e]
    bo=False
    if t==1:
        if d[a]<d[b]:
            bo=True
        else:
            a,b=b,a
    else:
        if d[b]<d[a]:
            bo=True
            a,b=b,a
    if bo:
        ans[b]-=x
        z+=x
    else:
        ans[b]+=x
p=[-1]*(n+1)
p[1]=z
q=[1]
while q:
    i=q.pop()
    for j in tree[i]:
        if p[j]==-1:
            p[j]=p[i]+ans[j]
            q.append(j)
for i in p[1:]:
    print(i)
        



