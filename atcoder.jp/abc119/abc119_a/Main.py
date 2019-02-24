s=input()
y=int(s[0:4])
m=int(s[5:7])
d=int(s[8:10])

if y<=2018:
    print("Heisei")
elif y==2019 and m<=4:
    print("Heisei")
else:
    print("TBD")