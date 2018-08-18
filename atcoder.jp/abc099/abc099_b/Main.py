a,b=map(int,input().split())

def m(x):
    return x*(x+1)/2

print(int(m(b-a-1)-a))