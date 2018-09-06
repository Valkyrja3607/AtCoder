n=int(input())
a=[int(i) for i in input().split()]

a.sort()

ans1=max(a)
ans2=0
b=0
c=0
lb=[]
lc=[]

if ans1%2==0:
    b=ans1/2
    c=ans1/2
else:
    b=(ans1+1)/2
    c=b-1

for i in a:
    if abs(i-b)<abs(ans2-b):
        ans2=i
    if abs(i-c)<abs(ans2-c):
        ans2=i

print(str(ans1)+" "+str(ans2))

