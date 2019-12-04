l,x,y,s,d=[int(j) for j in input().split()]
if s<=d:
    if y-x>0:
        print(min((d-s)/(x+y),(l+s-d)/(y-x)))
    else:
        print((d-s)/(x+y))
else:
    if y-x>0:
        print(min((l-s+d)/(x+y),(s-d)/(y-x)))
    else:
        print((l-s+d)/(x+y))