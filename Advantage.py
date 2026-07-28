t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mx = max(a)
    cnt = a.count(mx)
    second = -1
    for x in a:
        if x != mx:
            second = max(second, x)
    ans = []
    for x in a:
        if x == mx:
            if cnt > 1:
                ans.append(0)
            else:
                ans.append(x - second)
        else:
            ans.append(x - mx)
    print(*ans)
