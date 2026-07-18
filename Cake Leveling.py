t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    answer = []
    minimum = float("inf")
    for i in range(n):
        total += a[i]
        current_average = total // (i + 1)
        minimum = min(minimum, current_average)
        answer.append(minimum)
    print(*answer)
