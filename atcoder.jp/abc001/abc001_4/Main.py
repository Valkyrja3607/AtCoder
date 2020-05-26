n=int(input())
t=60*24+2
table=[0]*t
for i in range(n):
    a,b=[int(j)for j in input().split("-")]
    a=60*(a//100)+a%100-a%5
    if b%5:
        b=60*(b//100)+b%100+5-b%5
    else:
        b=60*(b//100)+b%100
    table[a]+=1
    table[b]-=1
b=False
for i in range(t):
    table[i]+=table[i-1]
    if table[i]!=0:
        if b:
            continue
        else:
            print(str(100*(i//60)+i%60).rjust(4,'0'),end="-")
            b=True
    else:
        if b:
            print(str(100*(i//60)+i%60).rjust(4,'0'))
            b=False
        else:
            continue