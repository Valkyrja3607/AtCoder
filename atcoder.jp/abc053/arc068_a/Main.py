x=int(input())

ans=(x//11)*2

if x%11>=7:
    ans+=2
elif x%11==0:
    ans+=0
else:
    ans+=1

print(ans)
    






