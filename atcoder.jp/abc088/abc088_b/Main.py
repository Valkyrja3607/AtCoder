n=int(input())
a=[int(j) for j in input().split()]
a.sort()
a.reverse()
alice,bob=0,0
for i in range(n):
    if i%2==0:
        alice+=a[i]
    else:
        bob+=a[i]
print(alice-bob)