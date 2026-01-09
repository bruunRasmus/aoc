lo,hi = [231832,767346]
ans1 = ans2 = 0
for n in range(lo,hi+1):
    n = str(n)
    FLAG1 = FLAG2 = False
    i = 0
    while i <len(n):
        if i>0 and int(n[i-1])>int(n[i]):
            break
        j = 1
        while j< len(n)-i:
            if n[i+j] != n[i]:
                break
            j+=1

        FLAG1 = FLAG1 or j >= 2
        FLAG2 = FLAG2 or j == 2
        i+=j

    else:
        ans1 += FLAG1
        ans2 += FLAG2



print(ans1)
print(ans2)