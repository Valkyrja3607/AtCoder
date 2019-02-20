n=int(input())
a=[int(i) for i in input().split()]

def f(l):
    m=min(l)
    li=[m]
    if m==sum(l):
        return m
    else:
        for i in range(len(l)):
            if l[i]%m!=0:
                li.append(l[i]%m)
        return f(li)

print(f(a))