a,b,c=map(int,input().split())
if pow(a,c%2+2)>pow(b,c%2+2):
    print(">")
elif pow(a,c%2+2)<pow(b,c%2+2):
    print("<")
else:
    print("=")