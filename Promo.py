n, q = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + p[i]
for _ in range(q):
    x, y = map(int, input().split())
    start = n - x
    end = start + y
    answer = prefix[end] - prefix[start]
    print(answer)
