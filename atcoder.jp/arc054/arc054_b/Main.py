p=float(input())
from math import *
x=max(0,1.5*log2(p*log(2)/1.5))
print(x+p/(2**(x/1.5)))