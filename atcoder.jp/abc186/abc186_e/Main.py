t=int(input())
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def chineseRem(b1, m1, b2, m2):
    d, p, q = egcd(m1, m2)
    if (b2 - b1) % d != 0:
        return 0, -1
    m = m1 * (m2 // d)
    tmp = (b2-b1) // d * p % (m2 // d)
    r = (b1 + m1 * tmp) % m
    return r, m

for i in range(t):
    n,s,k=map(int,input().split())
    r,m=chineseRem(-s,n,0,k)
    if m==-1:
        print(-1)
    else:
        print(r//k)