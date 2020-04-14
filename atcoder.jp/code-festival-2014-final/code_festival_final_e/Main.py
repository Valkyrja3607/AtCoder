n=int(input())
a=[int(j) for j in input().split()]
tmp=a[0]
ans=1
if n<3:
    print(0)
    exit()
while a[0]==a[1]:
    del a[0]
    if len(a)<3:
        print(0)
        exit()

high=False
if a[0]>a[1]:
    high=True

for i in a[1:]:
    if high:
        if tmp<i:
            tmp=i
        elif tmp>i:
            tmp=i
            ans+=1
            high=False
    else:
        if tmp>i:
            tmp=i
        elif tmp<i:
            tmp=i
            ans+=1
            high=True

if ans<3:
    print(0)
else:
    print(ans)


    