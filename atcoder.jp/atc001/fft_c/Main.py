import numpy as np
from numpy.fft import rfft,irfft
import sys
input=sys.stdin.readline

n=int(input())
ab=np.array([[int(j) for j in input().split()]for i in range(n)],np.int64)
a=ab[:,0]
b=ab[:,1]


fft_len=2*10**5
 
x=irfft(rfft(a,fft_len)*rfft(b,fft_len))
 
print(0)
print('\n'.join(map(str,(x[:n+n-1]+.5).astype(int))))
