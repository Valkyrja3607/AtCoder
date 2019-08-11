n=int(input())
hs=[]
l=[]
h=[]
for i in range(n):
    p=[int(j) for j in input().split()]
    hs.append(p)
    l.append(p[0]+p[1]*(n-1))
    h.append(p[0])
l.sort()

def f(x):
    t=[]
    for i in range(n):
        t.append((x-hs[i][0])//hs[i][1])
    t.sort()
    for i in range(n):
        if t[i]<i:
            return False
    return True

left=0
right=10**15
while right-left>1:
    p=(left+right)//2
    if f(p):
        right=p
    else:
        left=p
print(right)