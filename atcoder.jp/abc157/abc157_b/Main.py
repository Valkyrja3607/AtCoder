a=[[int(j) for j in input().split()]for i in range(3)]
n=int(input())
s=set()
for i in range(n):
    b=int(input())
    for j in range(3):
        for k in range(3):
            if a[j][k]==b:
                s.add((j+1,k+1))

for i in range(1,4):
    p,q=0,0
    for j in range(1,4):
        if (i,j) in s:
            p+=1
        if (j,i) in s:
            q+=1
    if p==3 or q==3:
        print("Yes")
        exit()
p,q=0,0
for i in range(1,4):
    if (i,i) in s:
        p+=1
    if (i,4-i) in s:
        q+=1
if p==3 or q==3:
    print("Yes")
    exit()

print("No")