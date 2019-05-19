n,k=map(int,input().split())
s=input()

if s[k-1]=="A":
    print(s[0:k-1]+"a"+s[k:n])
elif s[k-1]=="B":
    print(s[0:k-1]+"b"+s[k:n])
elif s[k-1]=="C":
    print(s[0:k-1]+"c"+s[k:n])
