n=input()
def f(s):
    for i,j in zip(s,s[::-1]):
        if i!=j:
            return False
    return True

for i in range(10):
    if f("0"*i+n):
        print("Yes")
        exit()
print("No")