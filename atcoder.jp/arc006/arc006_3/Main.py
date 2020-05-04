n=int(input())
l=[10**18]
for i in range(n):
    w=int(input())
    for idx,j in enumerate(l):
        if j>=w:
            l[idx]=w
            break
    l.sort()
    if l[-1]<w:
        l.append(w)
print(len(l))