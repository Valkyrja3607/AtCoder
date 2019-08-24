m,d=[int(j) for j in input().split()]
if d<=21:
    print(0)
    exit()
ans=0
for i in range(1,m+1):
    for j in range(22,d+1):
        d1=int(str(j)[1])
        d2=int(str(j)[0])
        if i==d1*d2 and d1>=2 and d2>=2:
            ans+=1
print(ans)



