lines = open("input.txt").read().strip().splitlines()
P = len(lines[0])

l = h = 0
O = S = 0
oxygen = scrubber = lines
for i in range(P):
    most_common_bit = sum([int(lines[j][i]) for j in range(len(lines))])>=len(lines)//2
    h+= 2**(P-i-1) * most_common_bit
    l+= 2**(P-i-1) * (1-most_common_bit)
    
    most_common_oxygen_bit = sum([int(o[i]) for o in oxygen])>=(len(oxygen)/2)
    least_common_scrubber_bit = sum([int(s[i]) for s in scrubber])<(len(scrubber)/2)
    oxygen = [oxygen[j] for j in range(len(oxygen)) if int(oxygen[j][i]) == most_common_oxygen_bit or len(oxygen) == 1]
    scrubber = [scrubber[j] for j in range(len(scrubber)) if int(scrubber[j][i]) == least_common_scrubber_bit or len(scrubber) == 1]

    O += 2**(P-i-1)*int(oxygen[0][i]) 
    S += 2**(P-i-1)*int(scrubber[0][i]) 

print(l*h)
print(S*O)