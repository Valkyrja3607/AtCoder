n=list(map(int,list(input())))
ans=0
for i in n:
    ans=(ans+i)%9
if ans==0:
    print("Yes")
else:
    print("No")