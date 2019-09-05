n=int(input())
d,x=map(int,input().split())
a=[int(input()) for i in range(n)]
x+=n
for i in a:
    x+=(d-1)//i
print(x)
