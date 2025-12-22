lines = open("input.txt").read().strip()
lines,y = lines.split(", y=")
_,x = lines.split("x=")
x1,x2 = [int(z) for z in x.split("..")]
y2,y1 = [int(z) for z in y.split("..")]

def inside(x_velo,y_velo):
    x_pos,y_pos = 0,0
    max_y = y_pos
    while y_pos >= y2 and x_pos <= x2:
        if x1<=x_pos<=x2 and y1>=y_pos>=y2:
            return max_y
        x_pos+=x_velo
        y_pos+=y_velo
        if x_velo >0:
            x_velo-=1
        elif x_velo < 0:
            x_velo +=1

        y_velo -= 1
        max_y = max(max_y,y_pos)
    return -1

ans1 = ans2 =  0
for init_x in range(x2+1):
    for init_y in range(y2,100):
        h = inside(init_x,init_y)
        ans1  = max(h,ans1)
        if h>=0:
            ans2+=1
print(ans1)
print(ans2) 