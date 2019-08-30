n,k=map(int,input().split())
d=[int(i) for i in input().split()]
d=set(d)
i=0
while True:
    s=str(n)
    c=0
    for i in s:
        if int(i) in d:
            break
        else:
            c+=1
    if c==len(s):
        print(n)
        exit()
    n+=1