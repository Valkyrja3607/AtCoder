n,k,m=map(int,input().split());a=m*n-sum(list(map(int,input().split())))
if a>k:print(-1)
else:print(max(0,a))