s=input()
l=[]
for i in s:
    if i=="0":
        l.append("0")
    elif i=="1":
        l.append("1")
    else:
        if l:
            del l[-1]
print("".join(l))