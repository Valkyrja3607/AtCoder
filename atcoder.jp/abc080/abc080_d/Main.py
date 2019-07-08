n,c=map(int,input().split())
stc=[[] for i in range(c+1)]
a=[]
t=0
for i in range(n):
    p=[int(j) for j in input().split()]
    stc[p[2]].append([p[0],p[1]])
    t=max(t,p[1])
ans=10**100
for i in range(c+1):
    p=10**10
    stc[i].sort()
    for j in range(len(stc[i])):
        if j+1<len(stc[i]):
            if stc[i][j][1]==stc[i][j+1][0]:
                if p==10**10:
                    p=stc[i][j][0]
            else:
                if p!=10**10:
                    a.append([p,stc[i][j][1]])
                else:
                    a.append([stc[i][j][0],stc[i][j][1]])
                p=10**10
        else:
            if p!=10**10:
                a.append([p,stc[i][j][1]])
            else:
                a.append([stc[i][j][0],stc[i][j][1]])

table=[0]*(t+1)
for i in range(len(a)):
    table[a[i][0]-1]+=1
    table[a[i][1]]-=1
for i in range(1,t+1):
    table[i]+=table[i-1]

print(max(table))


