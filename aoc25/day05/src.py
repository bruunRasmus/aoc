import bisect

ranges,vals = open("input.txt",'r').read().strip().split("\n\n")

ranges =[list(map(lambda x: int(x),r.split("-"))) for r in ranges.split("\n")]
vals = sorted([int(x) for x in vals.split("\n")]) 

ans1 = ans2 = 0

for l,h in ranges: 
    a = bisect.bisect_left(vals,l) 
    b = bisect.bisect_right(vals,h)
    for x in range(b,a,-1):
        del vals[x-1]  
        ans1+=1

non_overlapping_ranges = []

for l,h in ranges:
    to_remove= []
    for i in range(len(non_overlapping_ranges)):
         ll,hh = non_overlapping_ranges[i]
         if not (h < ll or hh < l):
            l,h = min(l,ll),max(h,hh)
            to_remove.append(i)
    for i in reversed(to_remove):
        del non_overlapping_ranges[i]
    non_overlapping_ranges.append([l,h])

for l,h in non_overlapping_ranges:
    ans2+=h-l+1

print(ans1)
print(ans2)