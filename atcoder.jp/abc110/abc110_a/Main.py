a,b,c=map(int,input().split())
m=max(a,b,c)
n=min(a,b,c)
l=a+b+c-m-n

print(10*m+l+n)