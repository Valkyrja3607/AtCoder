n=int(input())
a=set([int(input()) for i in range(3)])
c=0
if n>=301 or (n in a):
    print("NO")
    exit()
for i in range(100):
    if n-3 not in a:
        n-=3
    elif n-2 not in a:
        n-=2
    elif n-1 not in a:
        n-=1
    else:
        print("NO")
        exit()
    if n<=0:
        print("YES")
        exit()
print("NO")


