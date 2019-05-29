sa=list(input())
sb=list(input())
sc=list(input())

def f(a):
    if a=="a":
        if sa==[]:
            print("A")
        else:
            p=sa[0]
            del sa[0]
            f(p)
    if a=="b":
        if sb==[]:
            print("B")
        else:
            p=sb[0]
            del sb[0]
            f(p)
    if a=="c":
        if sc==[]:
            print("C")
        else:
            p=sc[0]
            del sc[0]
            f(p)

f("a")
