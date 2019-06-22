s=input()
p=""
q=0
for i in s:
    if p==i:
        q=1
    p=i
if q==1:
    print("Bad")
else:
    print("Good")