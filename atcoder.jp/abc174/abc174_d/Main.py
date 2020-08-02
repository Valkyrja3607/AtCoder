n=int(input())
c=input()
r=c.count("R")
w=n-r
ans=0
for i,j in zip(c,"R"*r+"W"*w):
    if i!=j:
        ans+=1
print(ans//2)