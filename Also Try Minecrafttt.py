n, m = map(int, input().split())
a = list(map(int, input().split()))
left_to_right = [0] * n
for i in range(1, n):
    if a[i - 1] > a[i]:
        left_to_right[i] = left_to_right[i - 1] + (a[i - 1] - a[i])
    else:
        left_to_right[i] = left_to_right[i - 1]
right_to_left = [0] * n
for i in range(n - 2, -1, -1):
    if a[i + 1] > a[i]:
        right_to_left[i] = right_to_left[i + 1] + (a[i + 1] - a[i])
    else:
        right_to_left[i] = right_to_left[i + 1]
for _ in range(m):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    if s < t:
        print(left_to_right[t] - left_to_right[s])
    else:
        print(right_to_left[t] - right_to_left[s])
