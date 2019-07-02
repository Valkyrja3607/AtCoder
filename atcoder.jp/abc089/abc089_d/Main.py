h,w,d=map(int,input().split())
a=[]
l=[[] for i in range(h*w+1)]
for i in range(h):
    p=[int(j) for j in input().split()]
    a.append(p)
    for j in range(w):
        l[int(p[j])].append(i)
        l[int(p[j])].append(j)
cost=[0 for i in range(h*w+1)]
for i in range(1,h*w+1-d):
    cost[i+d]=cost[i]+abs(l[i+d][0]-l[i][0])+abs(l[i][1]-l[i+d][1])
q=int(input())
lr=[]
for i in range(q):
    lr=[int(j) for j in input().split()]
    print(cost[lr[1]]-cost[lr[0]])