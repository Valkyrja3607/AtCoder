n,*a=map(int,open(0).read().split());r,m=1,10**9+7
if sum(a)!=n*2-2:r=0
for i in range(1,n-1):r=r*i%m
print(r*pow(2,m-1-a.count(3),m)%m)