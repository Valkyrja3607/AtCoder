n=int(input())
l=[int(i)%2 for i in input().split()]
if l.count(1)%2==0:
    print("YES")
else:
    print("NO")
