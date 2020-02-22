m=int(input())
l=[[int(j) for j in input().split()] for i in range(m)]
n=int(input())
ll=[tuple(int(j) for j in input().split()) for i in range(n)]
s=set(ll)

for i,j in ll:
    p,q=l[0]
    x,y=i-p,j-q
    ss=set()
    for t,u in l:
        ss.add((t+x,u+y))
    if len(ss&s)==m:
        print(x,y)
        exit()


