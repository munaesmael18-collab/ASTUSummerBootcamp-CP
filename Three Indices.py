t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    left = [-1] * n
    right = [-1] * n
    min_idx = 0
    for i in range(1, n):
        if p[min_idx] < p[i]:
            left[i] = min_idx
        if p[i] < p[min_idx]:
            min_idx = i
    min_idx = n - 1
    for i in range(n - 2, -1, -1):
        if p[min_idx] < p[i]:
            right[i] = min_idx
        if p[i] < p[min_idx]:
            min_idx = i
    found = False
    for j in range(n):
        if left[j] != -1 and right[j] != -1:
            print("YES")
            print(left[j] + 1, j + 1, right[j] + 1)
            found = True
            break
    if not found:
        print("NO")
