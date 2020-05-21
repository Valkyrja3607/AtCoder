s=list(input().split())
n=int(input())
for _ in range(n):
    f=input()
    m=len(f)
    for i,w in enumerate(s):
        c=0
        if len(w)==m:
            for p,q in zip(w,f):
                if q=="*" or p==q:
                    c+=1
                else:
                    break
        if c==m:
            s[i]="*"*m
print(*s)