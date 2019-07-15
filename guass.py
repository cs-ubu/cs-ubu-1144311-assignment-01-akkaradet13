import sys
from readfile import readfile

fileA = sys.argv[1]
fileB = sys.argv[2]

mA = readfile(fileA)
mb = readfile(fileB)

def guass(a,b):
    n = len(a)
    for k in range(0, n-1):
        for i in range(k+1, n):
            if a[i][k] != 0.0:
                lam = a[i][k]/a[k][k]
                print(lam)
                #a[i,k+1:n] = a[i, k+1:n] - lam*a[k,k+1:n]
                #b[i] = b[i] - lam*b[k]

guass(mA,mb)