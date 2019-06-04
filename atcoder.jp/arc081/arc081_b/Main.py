n=int(input())
s1=input()
s2=input()

ans=1
i=0
b=0
while i<n:
    if s1[i]==s2[i]:
        if b==0:
            ans*=3
        elif b==1:
            ans*=2
        else:
            ans*=1
        b=1
        i+=1
    else:
        if b==0:
            ans*=6
        elif b==1:
            ans*=2
        else:
            ans*=3
        b=2
        i+=2
    ans=ans%(10**9+7)
print(ans)
            
    
    





