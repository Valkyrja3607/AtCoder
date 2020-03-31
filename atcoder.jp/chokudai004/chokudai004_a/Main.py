n,b1,b2,b3=map(int,input().split())
l=list(list(map(int,input().split())) for i in range(n))
r=list(list(map(int,input().split())) for i in range(n))
for i in range(n):
    print(*r[i])