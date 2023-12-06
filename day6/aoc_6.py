import numpy as np
import sys

def possibleWins(m,k):
    lower = np.floor(((m-np.sqrt((m**2)-4*k))/2)+1)
    upper = np.ceil(((m+np.sqrt((m**2)-4*k))/2)-1)
    return upper - lower + 1

def results(file):
    f = open(file,'r')
    r = [line.split(":")[1].replace(" ","") for line in f]
    return(possibleWins(int(r[0]),int(r[1])))
    #pairs = zip(*r)
    #prod = 1
    #for p in pairs:
    #    m,k = p
    #    prod *= possibleWins(int(m),int(k))
    #return prod
print(results(sys.argv[1]))     
            