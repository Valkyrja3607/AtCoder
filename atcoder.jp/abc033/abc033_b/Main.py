n=int(input())
t=0
s=0
ans=""
for i in range(n):
    a,b=input().split()
    s+=int(b)
    if t<int(b):
        t=int(b)
        ans=a
if s/2<t:
    print(ans)
else:
    print("atcoder")