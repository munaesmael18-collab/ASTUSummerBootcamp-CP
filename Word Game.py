t = int(input())
for _ in range(t):
    n = int(input())
    players = []
    count = {}
    for _ in range(3):
        words = input().split()
        players.append(words)
        for word in words:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
    scores = []
    for words in players:
        score = 0
        for word in words:
            if count[word] == 1:
                score += 3
            elif count[word] == 2:
                score += 1
        scores.append(score)
    print(scores[0], scores[1], scores[2])
