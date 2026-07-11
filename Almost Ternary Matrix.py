import sys
def solve():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        
        for i in range(n):
            row = []
            for j in range(m):
                val_i = 1 if (i % 4 == 0 or i % 4 == 3) else 0
                val_j = 1 if (j % 4 == 0 or j % 4 == 3) else 0
                if val_i == val_j:
                    row.append("1")
                else:
                    row.append("0")
            out.append(" ".join(row))
    print("\n".join(out))
if __name__ == '__main__':
    solve()
