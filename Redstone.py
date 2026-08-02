t = int(input())
for _ in range(t):
    n = int(input())
    gears = list(map(int, input().split()))
    freq = {}
    ok = False
    for x in gears:
        if x in freq:
            ok = True
            break
        freq[x] = 1
    if ok:
        print("YES")
    else:
        print("NO")
