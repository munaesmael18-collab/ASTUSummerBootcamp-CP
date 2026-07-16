t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    pos = p.index(n)
    ok = True
    for i in range(pos):
        if p[i] > p[i + 1]:
            ok = False
            break
    if ok:
        for i in range(pos, n - 1):
            if p[i] < p[i + 1]:
                ok = False
                break
    print("YES" if ok else "NO")
