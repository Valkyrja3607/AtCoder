n=int(input())
l=[[int(j)for j in input().split()]for i in range(n)]
m=int(input())
op=[[int(j)for j in input().split()]+[0]for i in range(m)]
ll=[((0,0),(1,0),(0,1),0)]
for i in range(m):
    o,p=op[i][:2]
    ax,ay=ll[-1][0]
    bx,by=ll[-1][1]
    cx,cy=ll[-1][2]
    q=ll[-1][3]
    if o==1:
        ax,ay=ay,-ax
        bx,by=by,-bx
        cx,cy=cy,-cx
        q^=1
    elif o==2:
        ax,ay=-ay,ax
        bx,by=-by,bx
        cx,cy=-cy,cx
        q^=1
    elif o==3:
        ax,ay=2*p-ax,ay
        bx,by=2*p-bx,by
        cx,cy=2*p-cx,cy
    else:
        ax,ay=ax,2*p-ay
        bx,by=bx,2*p-by
        cx,cy=cx,2*p-cy
    ll.append(((ax,ay),(bx,by),(cx,cy),q))

Q=int(input())
for i in range(Q):
    a,b=map(int,input().split())
    ax,ay=ll[a][0]
    bx,by=ll[a][1]
    cx,cy=ll[a][2]
    qq=ll[a][3]
    x,y=l[b-1]
    p,q=bx-ax,by-ay
    r,s=cx-ax,cy-ay
    if qq==0:
        print(ax+x*p,ay+y*s)
    else:
        print(ax+y*r,ay+x*q)