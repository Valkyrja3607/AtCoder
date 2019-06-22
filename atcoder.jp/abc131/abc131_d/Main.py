n=int(input())
ab=[]
for i in range(n):
    a=[int(j) for j in input().split()]
    ab.append(a)

from operator import itemgetter
ab.sort(key=itemgetter(1))

p=0
for i in range(n):
    p+=ab[i][0]
    if ab[i][1]<p:
        print("No")
        import sys
        sys.exit()

print("Yes")