n,d,k=[int(j) for j in input().split()]
lr=[]
for i in range(d):
    lr.append([int(j) for j in input().split()])
ans=[]
for _ in range(k):
    s,t=[int(j) for j in input().split()]
    if s<t:
        tmp=s
        for i in range(d):
            l,r=lr[i]
            if l<=tmp<=r:
                tmp=r
            if tmp>=t:
                ans.append(i+1)
                break
    else:
        tmp=s
        for i in range(d):
            l,r=lr[i]
            if l<=tmp<=r:
                tmp=l
            if tmp<=t:
                ans.append(i+1)
                break
for i in ans:
    print(i)




