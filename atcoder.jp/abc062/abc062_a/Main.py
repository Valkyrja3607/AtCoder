x,y=map(int,input().split())
l=[1,3,5,7,8,10,12]
m=[4,6,9,11]
n=[2]
if x in l:
    if y in l:
        print("Yes")
        import sys
        sys.exit()
if x in m:
    if y in m:
        print("Yes")
        import sys
        sys.exit()
print("No")