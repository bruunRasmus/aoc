lines =  open("input.txt").read().strip().splitlines()

cuboids = []
for line in lines:
    op, rest = line.split(" ", 1)
    ranges = rest.replace("x=", "").replace("y=", "").replace("z=", "").split(",")
    x, y, z = ([int(v) for v in r.split("..")] for r in ranges)
    cuboids.append((op, (x, y, z)))

def intersect(c1, c2):
    result = []
    for a, b in zip(c1, c2):
        left = max(a[0], b[0])
        right = min(a[1], b[1])
        if left > right:
            return None
        result.append([left, right])
    return result

def non_intersecting_cuboid(c1, c2):
    inter = intersect(c1, c2)
    if inter is None:
        return [c1]

    (x1, y1, z1) = c1
    (x2, y2, z2) = inter

    pieces = [
        ([x1[0], x2[0] - 1], y1, z1),
        ([x2[1] + 1, x1[1]], y1, z1),

        (x2, [y1[0], y2[0] - 1], z1),
        (x2, [y2[1] + 1, y1[1]], z1),

        (x2, y2, [z1[0], z2[0] - 1]),
        (x2, y2, [z2[1] + 1, z1[1]]),
    ]

    return [c for c in pieces if all(lo <= hi for lo, hi in c)]

on = []
for op, c2 in cuboids:
    updated = []
    for c1 in on:
        updated.extend(non_intersecting_cuboid(c1, c2))
    if op == "on":
        updated.append(c2)
    on = updated

ans1 = ans2 = 0
for cuboid in on:
    v1 = v2 = 1
    for lo, hi in cuboid:
        v2 *= hi - lo + 1
        if hi < -50 or lo > 50:
            v1 = 0
        else:
            v1 *= min(hi, 50) - max(lo, -50) + 1

    ans1 += v1
    ans2 += v2

print(ans1)
print(ans2)