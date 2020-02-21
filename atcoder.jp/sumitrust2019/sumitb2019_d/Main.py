n=int(input())
s=input()
l=[[] for i in range(10)]
for i in range(n):
    j=int(s[i])
    l[j].append(i)
ans=0
for i in range(1000):
    i=str(i).rjust(3,"0")
    a,b,c=[int(j) for j in i]
    if l[a] and l[b] and l[c]:
        p,q=l[a][0],l[c][-1]
        if p<q:
            for j in l[b]:
                if p<j<q:
                    ans+=1
                    break
print(ans)
