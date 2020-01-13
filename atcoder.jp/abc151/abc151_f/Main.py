from scipy.optimize import*
from numpy import*
n=int(input())
l=array([list(map(int,input().split()))for i in range(n)])
def f(a):
    return ((l-a)**2).sum(1).max()**0.5
print(minimize(f,[0,0],method="Nelder-Mead",tol=1e-9).fun)