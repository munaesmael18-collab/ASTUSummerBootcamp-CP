t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    array = list(map(int, input().split()))
    total_sum = sum(array)
    prefix = [0]
    for num in array:
        prefix.append(prefix[-1] + num)
    for _ in range(q):
        l, r, k = map(int, input().split())
        length = r - l + 1
        segment_sum = prefix[r] - prefix[l - 1]
        new_sum = total_sum - segment_sum + length * k
        if new_sum % 2 == 1:
            print("YES")
        else:
            print("NO")
