a,v=[int(j)for j in input().split()]
b,w=[int(j)for j in input().split()]
t=int(input())
p=abs(a-b)
if v-w<0:
    print("NO")
else:
    if t*(v-w)>=p:
        print("YES")
    else:
        print("NO")

