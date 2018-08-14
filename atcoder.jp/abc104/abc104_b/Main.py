s=input()
l=len(s)
j=0
k=0

if s[0]=="A":
    for i in range(2,l-1):
        if s[i]=="C":
            j=i
            k+=1

if k==1:
    if s[1:j].islower() and s[j+1:l].islower():
        print("AC")
    else:
        print("WA")
else:
    print("WA")