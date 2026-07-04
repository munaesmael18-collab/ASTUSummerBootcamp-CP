t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    blocks = 1
    has_equal = False

    for i in range(1, n):
        if s[i] != s[i - 1]:
            blocks += 1
        else:
            has_equal = True

    if not has_equal:
        print(blocks)
    elif s[0] == s[-1]:
        print(blocks)
    else:
        print(blocks + 1)
