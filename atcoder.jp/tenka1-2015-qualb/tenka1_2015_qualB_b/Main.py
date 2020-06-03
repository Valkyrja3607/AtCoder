s=input()
if s=="{}":
    print("dict")
    exit()
t=""
b=0
for i in s[1:-1]:
    if b==0 and i!="{":
        t+=i
    elif i=="}":
        b-=1
    elif i=="{":
        b+=1
t="{"+t+"}"

if ":" in t:
    print("dict")
else:
    print("set")