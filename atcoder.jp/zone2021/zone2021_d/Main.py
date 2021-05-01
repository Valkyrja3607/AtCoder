s=input()
c=0
t=""
for i in s:
    if i!="R":
        if c==0:
            if t and t[-1]==i:
                t=t[:-1]
            else:
                t+=i
        else:
            if t and t[0]==i:
                t=t[1:]
            else:
                t=i+t
    else:
        c+=1
        c%=2
if c==0:
    print(t)
else:
    print(t[::-1])