n,m,X,Y=map(int,input().split())

x=[int(i) for i in input().split()]
y=[int(i) for i in input().split()]

mx=max(x)
my=min(y)

if max(X,mx)<min(Y,my):
    print("No War")
else:
    print("War")