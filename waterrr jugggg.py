def water_jug(x,y,z):
    visited = set()
    queue = deque([(0,0)])

    while queue:
        juga,jugb = queue.popleft()

        if juga == z or jugb == z or juga+jugb == z:
            return True
        if (juga,jugb) in visited:
            continue
        
        visited.add((juga,jugb))

        if juga < x:
            queue.append((x,jugb))

        if jugb < y:
            queue.append((juga,y))

        if juga > 0:
            queue.append((0,jugb))

        if jugb > 0:
            queue.append((juga,0))

        if juga+jugb >= y:
            queue.append((juga - (y - jugb),y))
        else:
            queue.append((0,juga+jugb))

        if juga + jugb >= x:
            queue.append((x,jugb - (x - jugb)))
        else:
            queue.append((juga+jugb,0))
    return False

x = 6
y = 3
z = 2

if water_jug(x,y,z):
    print("YES")
else:
    print("NO")
