t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ans = n

    for c in "abcdefghijklmnopqrstuvwxyz":
        last = s.rfind(c)
        if last == -1:
            continue

        ok = True
        for i in range(last + 1, n):
            if s[i] != c:
                ok = False
                break

        if not ok:
            continue

        cnt = 0
        for i in range(last):
            if s[i] != c:
                cnt += 1

        ans = min(ans, cnt)

    print(ans)
