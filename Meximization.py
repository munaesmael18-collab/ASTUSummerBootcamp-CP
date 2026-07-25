t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    answer = []

    # Add 0, 1, 2, ... if they exist
    for x in range(101):
        if x in a:
            answer.append(x)
            a.remove(x)
        else:
            break

    # Add the remaining elements
    answer.extend(a)

    print(*answer)
