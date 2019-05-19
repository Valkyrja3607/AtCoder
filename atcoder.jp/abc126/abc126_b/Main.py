s=input()

def f(a):
    a=int(a)
    if a>0 and a<=12:
        return 0
    elif a>12 or a==0:
        return 1


if f(s[0:2])*f(s[2:4])==0:
    if f(s[0:2])==0 and f(s[2:4])==0:
        print("AMBIGUOUS")
    elif f(s[0:2])==1 and f(s[2:4])==0:
        print("YYMM")
    elif f(s[0:2])==0 and f(s[2:4])==1:
        print("MMYY")
else:
    print("NA")