n,k=map(int,input().split())
l=[]
for i in range(n):
    a,b=[int(j) for j in input().split()]
    l.append([a,b])
l.sort()
p=0
i=0
while True:
    if p+l[i][1]>=k:
        print(l[i][0])
        break
    else:
        p+=l[i][1]
        i+=1

