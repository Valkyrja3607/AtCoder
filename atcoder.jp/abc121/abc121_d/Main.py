a,b=map(int,input().split())

def f(n):
    p=0
    if n%2==1:
        p=(n+1)//2
        if p%2==0:
            return 0
        else:
            return 1
    else:
        p=n//2
        if p%2==0:
            return n^0
        else:
            return n^1

print(f(a-1)^f(b))