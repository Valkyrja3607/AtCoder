n=int(input())
tmp=[-10**9+1,10**9+1,-10**9+1,10**9+1]
for _ in range(n):
    a,t=map(int,input().split())
    if t==1:
        tmp[2]+=a
        tmp[3]+=a
    elif t==2:
        if tmp[2]<a<=tmp[3]:
            tmp[0]+=a-tmp[2]
            tmp[2]=a
        elif tmp[3]<=a:
            tmp[0]=tmp[1]
            tmp[2]=a
            tmp[3]=a
    else:
        if tmp[3]>a>tmp[2]:
            tmp[1]-=tmp[3]-a
            tmp[3]=a
        elif tmp[2]>=a:
            tmp[1]=tmp[0]
            tmp[2]=a
            tmp[3]=a
q=int(input())
x=[int(j)for j in input().split()]
a,b,c,d=tmp
for i in x:
    if a<i<b:
        print(i+c-a)
    elif i<=a:
        print(c)
    else:
        print(d)