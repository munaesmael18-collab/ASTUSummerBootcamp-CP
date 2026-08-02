t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    actions = list(map(int, input().split()))
    ans = [-1] * n
    seen = set()
    cnt = 0
    for time in range(1, m + 1):
        p = actions[time - 1]
        if p not in seen:
            seen.add(p)
            cnt += 1
            idx = n - cnt
            if idx >= 0:
                ans[idx] = time
    print(*ans)
