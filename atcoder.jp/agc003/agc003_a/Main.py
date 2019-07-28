s=input()
l=list(s)
N=l.count("N")
W=l.count("W")
S=l.count("S")
E=l.count("E")

if N*S!=0 and E*W!=0:
    print("Yes")
elif N*S==0 and E*W!=0:
    if N==0 and S==0:
        print("Yes")
    else:
        print("No")
elif E*W==0 and N*S!=0:
    if E==0 and W==0:
        print("Yes")
    else:
        print("No")
else:
    print("No")