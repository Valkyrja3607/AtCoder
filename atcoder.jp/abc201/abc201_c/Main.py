s=input()
x=s.count("o")
y=s.count("?")
if x>4 or x+y==0:
    print(0)
    exit()
ans=0
for i in range(10000):
    j=str(i).rjust(4,'0')
    a=set()
    b=True
    for k in j:
        if s[int(k)]=="o":
            a.add(k)
        elif s[int(k)]=="x":
            b=False
    if b:
        if len(a)==x:
            ans+=1
print(ans)





