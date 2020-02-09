n=int(input())
a=set([int(j) for j in input().split()])

if len(a)==n:
    print("YES")
else:
    print("NO")