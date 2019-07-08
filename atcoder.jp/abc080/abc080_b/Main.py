n=int(input())
def f(n):
    n=str(n)
    r=0
    for i in range(len(n)):
        r+=int(n[i])
    return r
if n%f(n)==0:
    print("Yes")
else:
    print("No")