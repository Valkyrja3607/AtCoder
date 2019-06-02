n,a,b,c,d=map(int,input().split())
s=input()
s2=s[min(a,b)-1:max(c,d)]
n2=len(s2)

sl=s[a-1:c]
sr=s[b-1:d]

for i in range(len(sl)-1):
    if sl[i]=="#" and sl[i+1]=="#":
        print("No")
        import sys
        sys.exit()
for i in range(len(sr)-1):
    if sr[i]=="#" and sr[i+1]=="#":
        print("No")
        import sys
        sys.exit()


if c<d:
    print("Yes")
else:
    for i in range(n2-2):
        if s2[i]=="." and s2[i+1]=="." and s2[i+2]=="." and i<d-1 and b<i+3:
            print("Yes")
            import sys
            sys.exit()
    print("No")