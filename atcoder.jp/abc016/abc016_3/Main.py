n,m=[int(j) for j in input().split()]
l=[set() for i in range(n)]
for i in range(m):
    a,b=[int(j)-1 for j in input().split()]
    l[a].add(b)
    l[b].add(a)

for i in range(n):
    ans=set()
    for j in l[i]:
        for k in l[j]:
            ans.add(k)
    ans=ans-l[i]
    if ans:
        print(len(ans)-1)
    else:
        print(0)