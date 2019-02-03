n,k=map(int,input().split())

td=[]

for i in range(n):
    a=[]
    a=[int(j) for j in input().split()]
    td.append(a)

from operator import itemgetter
td.sort(key=itemgetter(1))  
td.reverse()
td.sort(key=itemgetter(0))

s=0
l=[]
for i in range(n):
    if s!=td[i][0]:
        s=td[i][0]
        l.append([td[i][1],1])
    else:
        l.append([td[i][1],0])

l.sort(key=itemgetter(0))
l.reverse()

op=0
sp=0
ans=[]
sl=[]
l1=[]

for i in range(n):
    if i<k:
        op+=l[i][0]
        sp+=l[i][1]
        if l[i][1]==0:
            sl.append(l[i][0])
    else:
        if l[i][1]==1:
            l1.append(l[i][0])


ans=[op+sp**2]
sl.sort()
l1.sort()
l1.reverse()

for i in range(min(len(sl),len(l1))):
    ans.append(ans[-1]-sl[i]+l1[i]+sp*2+1)
    sp+=1

print(max(ans))





    

