lines = open("input.txt",'r').read().strip().split("\n")

ans1 = ans2 = 0

for L in [2,12]:
    for line in lines:
        digits = ["0" for _ in range(L)]
        for i in range (len(line)):
            d = line[i]
            for j in range(L):
                if d>digits[j] and len(line)-i >= L-j:
                    digits[j] = d
                    digits[j+1:] = ["0" for _ in range(L-j-1)]
                    break
        ans1 += int("".join(digits))
    print(ans1)