t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    distinct_problems = set(s)
    answer = n + len(distinct_problems)
    print(answer)
