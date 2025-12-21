lines = open("input.txt").read().strip().splitlines()
lines = [(s.split(), o.split()) for s, o in (l.split("|") for l in lines)]

ans1 = ans2 = 0
for signal,output in lines:
    digits = {}
    for d in signal:
        match len(d):
            case 2: digits[1] = d
            case 3: digits[7] = d
            case 4: digits[4] = d
            case 7: digits[8] = d

    code = ""
    for d in output:
        match len(d):
            case 2: code += "1"; ans1 += 1
            case 3: code += "7"; ans1 += 1
            case 4: code += "4"; ans1 += 1
            case 5:
                if all(segment in d for segment in digits[1]):
                    code += "3"
                elif sum(segment in d for segment in digits[4]) == 2:
                    code += "2"
                else:
                    code += "5"
            case 6:
                if all(segment in d for segment in digits[4]):
                    code += "9"
                elif all(segment in d for segment in digits[1]):
                    code += "0"
                else:
                    code += "6"
                    
            case 7: code += "8"; ans1 += 1       
    ans2+=int(code)
    
print(ans1)
print(ans2)