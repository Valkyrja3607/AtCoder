from collections import deque
n=int(input())
a=[int(i) for i in input().split()]
b=deque()
for i in range(n):
    if i%2==0:
        b.appendleft(a[i])
        
    else:
        b.append(a[i])

if n%2==0:
    b.reverse()

for i in range(n):
    if i!=n-1:
        print(b[i],end=" ")
    else:
        print(b[i])