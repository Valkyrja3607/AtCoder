from collections import defaultdict, deque
v,n=map(int,input().split())
es=[]
l=[[]for i in range(v)]
for i in range(n-1+v):
    a,b=[int(j)-1 for j in input().split()]
    es.append((a,b))
    l[a].append(b)
#頂点は0~v-1

outs = defaultdict(list)
ins = defaultdict(int)
for v1, v2 in es:
    outs[v1].append(v2)
    ins[v2] += 1

q = deque(v1 for v1 in range(v) if ins[v1] == 0)
res = []
while q:
    v1 = q.popleft()
    res.append(v1)
    for v2 in outs[v1]:
        ins[v2] -= 1
        if ins[v2] == 0:
            q.append(v2)

ans=[0]*v
s=set()
for i in res[::-1]:
    s.add(i)
    for j in l[i]:
        if j in s:
            ans[j]=i+1
            s.remove(j)

print('\n'.join(map(str,ans)))