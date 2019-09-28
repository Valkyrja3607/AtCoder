import sys
input = sys.stdin.readline
n,x,y=[int(j) for j in input().split()]
a=[int(j) for j in input().split()]
a=[y]+a
print(max(abs(y-a[-1]),abs(a[-2]-a[-1])))