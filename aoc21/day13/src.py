dots_file,folds = open("input.txt").read().strip().split("\n\n")

dots = set()
for d in dots_file.splitlines():
    x,y = [int(n) for n in d.split(",")]
    dots.add((x,y))

part1 = True
for f in folds.splitlines():
    dim,coord = f.split("=")
    dim = dim[-1:]
    coord = int(coord)
    
    new_dots = set()
    for x,y in dots:
        if dim == "x" and  x>coord:
            x = 2 * coord - x
        elif dim == "y" and y>coord: 
            y = 2 * coord - y   
        new_dots.add((x,y))
    dots = new_dots
    if part1:
        print(len(dots))
        part1 = False
    
xs, ys = zip(*dots)
Xmin, Xmax = min(xs), max(xs)
Ymin, Ymax = min(ys), max(ys)

for y in range(Ymin, Ymax + 1):
    for x in range(Xmin, Xmax + 1):
        print("#" if (x, y) in dots else ".", end="")
    print()
