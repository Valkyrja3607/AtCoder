A=int(input())
B=int(input())
C=int(input())
X=int(input())
x=X/50

n=0

for c in range(C+1):
    for b in range(B+1):
        for a in range(A+1):
            if(10*a+2*b+c==x):
                n += 1

print(n)