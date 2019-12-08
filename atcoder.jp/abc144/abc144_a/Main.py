import sys
input = sys.stdin.readline
a,b=[int(j) for j in input().split()]
if a<10 and b<10:
    print(a*b)
else:
    print(-1)