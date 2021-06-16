n=int(input())
l1=[0]
l2=[0]
for i in range(1,1+n):
    c,p=map(int,input().split())
    if c==1:
        l1.append(p+l1[-1])
        l2.append(0+l2[-1])
    else:
        l1.append(0+l1[-1])
        l2.append(p+l2[-1])
q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    print(l1[r]-l1[l-1],l2[r]-l2[l-1])