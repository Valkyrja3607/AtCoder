n,q=map(int,input().split())
s=input()
lr=[]
for i in range(q):
    a=[int(j) for j in input().split()]
    lr.append(a)

la=[0 for i in range(n)]
lc=[0 for i in range(n)]
x=0
y=0
for i in range(n-1):
    if s[i]=="A" and s[i+1]=="C":
        x+=1
        y+=1
        
    la[i]=x
    lc[i+1]=y
        
for i in range(q):
    print(min(la[lr[i][1]-2]-la[lr[i][0]-2],lc[lr[i][1]-1]-lc[lr[i][0]-1]))
    












