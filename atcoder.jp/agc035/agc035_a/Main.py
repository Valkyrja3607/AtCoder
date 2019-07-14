n=int(input())
a=[int(j) for j in input().split()]
import collections
c=collections.Counter(a)
l=c.most_common()
ll=[]
for i,j in l:
    ll.append(i)
if sum(ll)==0:
    print("Yes")
    exit()
if 0 in ll:
    if len(l)==2:
        for i,j in l:
            if i==0:
                z=j
            else:
                t=j
        if 2*z==t:
            print("Yes")
            exit()
        else:
            print("No")
            exit()
    else:
        print("No")
        exit()

p=l[0][1]
q=[]
if len(l)==3:
    for i,j in l:
        if j==p:
            q.append(i)
        else:
            print("No")
            exit()
else:
    print("No")
    exit()
if q[0]^q[1]==q[2] and q[0]^q[2]==q[1] and q[2]^q[1]==q[0]:
    print("Yes")
else:
    print("No")





