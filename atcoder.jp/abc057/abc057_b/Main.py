n,m=map(int,input().split())
ab=[]
cd=[]
for i in range(n):
    ab.append([int(j) for j in input().split()])
for i in range(m):
    cd.append([int(j) for j in input().split()])
a=[]
for i,j in ab:
    tmp=10**100
    ans=0
    k=1
    for x,y in cd:
        if tmp>abs(i-x)+abs(j-y):
            tmp=abs(i-x)+abs(j-y)
            ans=k
        k+=1
    a.append(ans)
for i in a:
    print(i)




