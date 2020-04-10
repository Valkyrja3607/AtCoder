a,b,c=map(int,input().split())
n=a+b+c
import itertools
ans=0
for x in itertools.permutations(range(n)):
    x=list(x)
    l1=x[:a]+[10,10]
    l2=x[a:a+b]+[10,10]
    l3=x[a+b:n]+[10,10]
    if l1[0]<=l1[1]<=l1[2] and l2[0]<=l2[1]<=l2[2] and l3[0]<=l3[1]<=l3[2]:
        if l1[0]<=l2[0]<=l3[0] and l1[1]<=l2[1]<=l3[1] and l1[2]<=l2[2]<=l3[2]:
            ans+=1
   
print(ans)