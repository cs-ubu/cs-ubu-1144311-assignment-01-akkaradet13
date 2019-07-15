def readfile(filename):
    f = open(filename,'r')
    A = []
    for line in f.readlines():
        A.append([float(x) for x in line.strip().split(',')])
    f.close
    return A