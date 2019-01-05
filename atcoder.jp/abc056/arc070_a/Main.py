x=int(input())

t=1
k=0
i=0

while k==0:
    i+=t
    t+=1
    if i>=x:
        k=1

print(t-1)

