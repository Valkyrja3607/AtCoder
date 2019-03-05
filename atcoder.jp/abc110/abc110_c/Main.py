s=input()
t=input()


def f(s):
    l=[]
    a="abcdefghijklmnopqrstuvwxyz"
    r=""
    for i in range(len(s)):
        if s[i] in l:
            for j in range(len(l)):
                if s[i]==l[j]:
                    r+=a[j]
        else:
            r+=a[len(l)]
            l.append(s[i])
    return r

if f(s)==f(t):
    print("Yes")
else:
    print("No")
