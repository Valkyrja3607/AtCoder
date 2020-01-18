l=[]
for i in range(int(input())):
    x,y=map(int,input().split())
    l.append((x+y,x-y))
l.sort()
t,a=l[0][1],0
for j,i in l:
    if t<=i:
        a+=1
        t=j
print(a)