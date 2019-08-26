n=int(input())
a=[int(i) for i in input().split()]
c2=0
c4=0
c=0
for i in a:
    if i%4==0:
        c4+=1
    elif i%2==0:
        c2+=1
    else:
        c+=1

if c==0 or c+c2-1<=c4 or c<=c4:
    print("Yes")
else:
    print("No")