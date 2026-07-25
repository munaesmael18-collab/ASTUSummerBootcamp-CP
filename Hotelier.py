n = int(input())
event = input()
room = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range (n):
    if event[i] == "L":
        for j in range(10):
            if room[j] == 0:
                room[j]=1
                break
    elif event[i] == "R":
        for j in range(9, -1, -1):
            if room[j] == 0:
                room[j]=1
                break
    else:
        room[int(event[i])] = 0
print("".join(map(str, room)))
