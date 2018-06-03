N=int(input())
a=[int(n) for n in input().split()]

A=0
B=0

if N%2==0:
    n=N/2
else:
    n=(N+1)/2
    a.append(0)

for i in range(int(n)):
    A += max(a)
    a.remove(max(a))
    B += max(a)
    a.remove(max(a))

print(A-B)