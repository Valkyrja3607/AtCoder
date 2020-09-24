n=int(input())
t=0
for i in range(n):
    a,b=input().split()
    if a==b:
        t+=1
    else:
        t=0
    if t==3:
        print("Yes")
        exit()
print("No")