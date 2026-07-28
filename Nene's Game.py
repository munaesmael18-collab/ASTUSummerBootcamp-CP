t = int(input())
for _ in range(t):
    k, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = list(map(int, input().split()))
    first = a[0] - 1
    ans = []
    for n in queries:
        ans.append(str(min(n, first)))
    print(*ans)
