import sys
spelledDigit = {"zero":"0",
                "one":"1", 
                "two":"2", 
                "three":"3", 
                "four":"4",
                "five":"5", 
                "six":"6", 
                "seven":"7", 
                "eight":"8", 
                "nine":"9"}


def deartify(s): 
    ds = digits(s)
    first = ds[0]
    last = ds[-1]
    return int(first+last)

def digits(s):
    retval = []
    length = len(s)
    for i in range (length):
        remainingChars = length - i
        if s[i].isdigit():
            retval.append(s[i])
        app = min(remainingChars,5)
        cs = checkSpelled(s[i:i+app])
        if cs[0]:
            retval.append(spelledDigit[cs[1]])
    return retval

def checkSpelled (s):
    if len(s) < 3:
        return (False,"")
    elif s in spelledDigit.keys():
        return (True,s)
    else:
        return checkSpelled (s[:-1])

f = open(sys.argv[1],"r")
sum = 0
for line in f:
    sum += deartify(line)
f.close()
print(sum)
