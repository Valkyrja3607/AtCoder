a,b,c=map(int,input().split())
i=1
while i<=a:
    if (b*i+c)%a==0:
        print("YES")
        exit()
    i+=1
print("NO")