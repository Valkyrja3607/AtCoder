q,h,c,d=map(int,input().split())
n=int(input())

o=min(4*q,2*h,c)
t=min(2*o,d)
if n%2==0:
    print(n*t//2)
else:
    print(t*(n//2)+o)





