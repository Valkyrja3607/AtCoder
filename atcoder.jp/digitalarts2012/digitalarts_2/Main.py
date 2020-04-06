s=input()
h=0
for i in s:
    h+=ord(i)-96
if h==1 or h==520:
	print("NO")
	exit()
h=sum(ord(x)-96 for x in s)
a="z"*(h//26)+chr(h%26+96)*(h%26>0)
if a==s:
	a=a[::-1]
if a==s:
	a=a[:-1]+chr(ord(a[-1])-1)+"a"
print(a)