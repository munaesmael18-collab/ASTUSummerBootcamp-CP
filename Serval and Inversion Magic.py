import sys

def solve():
    # Read n and the string s
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    blocks = 0
    in_mismatch_block = False
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            if not in_mismatch_block:
                blocks += 1
                in_mismatch_block = True
        else:
            in_mismatch_block = False
    if blocks <= 1:
        print("Yes")
    else:
        print("No")
def main():
    # Fast I/O
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        s = data[idx+1]
        idx += 2
        blocks = 0
        in_mismatch_block = False
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                if not in_mismatch_block:
                    blocks += 1
                    in_mismatch_block = True
            else:
                in_mismatch_block = False
                
        if blocks <= 1:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()
