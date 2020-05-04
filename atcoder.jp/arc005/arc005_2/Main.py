x,y,w=input().split()
x,y=int(y)-1,int(x)-1
c=[[j for j in input()]for i in range(9)]
ans=c[x][y]
i,j=0,0
if w=="R":
    j=1
if w=="L":
    j=-1
if w=="U":
    i=-1
if w=="D":
    i=1
if w=="RU":
    i,j=-1,1
if w=="RD":
    i,j=1,1
if w=="LU":
    i,j=-1,-1
if w=="LD":
    i,j=1,-1
for _ in range(3):
    x+=i
    y+=j
    if x<0:
        x=1
        i=1
    if x>8:
        x=7
        i=-1
    if y<0:
        y=1
        j=1
    if y>8:
        y=7
        j=-1
    ans+=c[x][y]

print(ans)