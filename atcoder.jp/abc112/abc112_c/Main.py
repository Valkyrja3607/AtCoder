n=int(input())
xyh=[]
h0=[]
for i in range(n):
    a=[int(j) for j in input().split()]
    xyh.append(a)

from operator import itemgetter
xyh.sort(key=itemgetter(2))
xyh.reverse()

for x in range(101):
    for y in range(101):
        p=0
        l=max(0,xyh[0][2]+abs(x-xyh[0][0])+abs(y-xyh[0][1]))
        for i in range(n):
            if xyh[i][2]==0:
                if l>abs(x-xyh[i][0])+abs(y-xyh[i][1]):
                    p=1
                    break
                else:
                    continue
            if l==max(0,xyh[i][2]+abs(x-xyh[i][0])+abs(y-xyh[i][1])):
                l=max(0,xyh[i][2]+abs(x-xyh[i][0])+abs(y-xyh[i][1]))
            else:
                p=1
                break
        if p==0:
            print(x,y,l)
            import sys
            sys.exit()
            

