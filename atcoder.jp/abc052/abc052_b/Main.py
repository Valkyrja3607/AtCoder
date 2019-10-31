n=int(input())
s=input()
x=0
tmp=0
for i in s:
    if i=="I":
        tmp+=1
    else:
        tmp-=1
    x=max(x,tmp)
print(x)

