n,m=map(int,input().split())
l=[True]*(n+1)
a=[int(input())for i in range(m)][::-1]
for i in a:
    if l[i]:
        l[i]=False
        print(i)
for i in range(1,1+n):
    if l[i]:
        print(i)