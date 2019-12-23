n,m=map(int,input().split())
a=abs(n%12*30-m*5.5)
print(min(a,360-a))