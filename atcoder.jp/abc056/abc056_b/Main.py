w,a,b=map(int,input().split())
if b<a:
    a,b=b,a
print(max(0,b-a-w))



