from math import ceil
from bisect import bisect_left,bisect_right

lines = open("input.txt",'r').read().strip()
lines = lines.split("\n")

pairs = lines[0].split(",")
ans1 = ans2 = 0

#Check all numbers in range
for p in pairs:
    fst_id,snd_id = p.split("-")
    for i in range(int(fst_id),int(snd_id)+1):
        str_i = str(i)
        for j in range(len(str_i)//2,0,-1):
            if len(str_i)%j != 0:
                continue
            substr = str_i[:j]
            if str_i == substr*(len(str_i)//j):
                if j == len(str_i)/2:
                    ans1+=i
                ans2+=i
                break

#Directly compute all valid numbers in range
ans1 = ans2 = 0
for p in pairs:
    lst = []
    fst_id,snd_id = p.split("-")
    for i in range(1,len(snd_id)//2+1):
        low = min(int(fst_id[0:i]),int(snd_id[0:i]),int("1"+"0"*(i-1)))
        high = min(int(snd_id[0:ceil(len(snd_id)/2)]),int("9"*i))
        for j in range(low,high+1):
            for k in range(max(len(fst_id),2)//i,len(snd_id)//i+1):
                guess = int(str(j)*k)
                if int(fst_id)<=guess <=int(snd_id) and guess not in lst:
                    lst.append(guess)
                    if str(guess)[0:len(str(guess))//2]*2 == str(guess):
                        ans1+=guess
    ans2+=sum(lst)
    

#Precompute all valid numbers, and BS for each pair    
N=0
for p in pairs:
    fst,snd = p.split("-")
    N=max(N,int(snd))

pn = sorted(list({
    int(str(p) * k)
    for L in range(1, len(str(N)) // 2 + 1)
    for p in range(10**(L-1), 10**L)             
    for k in range(2, len(str(N)) // L + 2)     
    if int(str(p) * k) <= N                    
}))
pns = sorted(list({
    int(str(p) * k)
    for L in range(1, len(str(N)) // 2 + 1) 
    for p in range(10**(L-1), 10**L)             
    for k in range(2, 3)     
    if int(str(p) * k) <= N                     
}))

ans1 = ans2 = 0
for p in pairs:
    fst,snd = p.split("-")
    ans2+=sum(pn[bisect_left(pn, int(fst)):bisect_right(pn, int(snd))])
    ans1+=sum(pns[bisect_left(pns, int(fst)):bisect_right(pns, int(snd))])