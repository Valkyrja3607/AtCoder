n=input()
ans=(len(n)-1)*9

p=0
for i in range(1,10):
    if i*10**(len(n)-1)+(10**(len(n)-1)-1)<=int(n):
        p=max(p,i)

print(ans+p)



