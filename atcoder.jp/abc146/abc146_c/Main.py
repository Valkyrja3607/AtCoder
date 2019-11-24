a,b,x=[int(j) for j in input().split()]
ans=0

if a*(10**9)+b*10<=x:
    print(10**9)
    exit()
for i in range(1,11):
    if x>b*i:
        n=x-b*i
        if len(str(n//a))==i:
            ans=n//a
        elif len(str(n//a))>i:
            ans=int("9"*i)

print(ans)

