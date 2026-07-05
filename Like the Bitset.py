import sys
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    out = []  
    for _ in range(t):
        n = int(input_data[idx])
        k = int(input_data[idx+1])
        s = input_data[idx+2]
        idx += 3
        max_ones = 0
        current_ones = 0
        for char in s:
            if char == '1':
                current_ones += 1
                if current_ones > max_ones:
                    max_ones = current_ones
            else:
                current_ones = 0                
        if max_ones >= k:
            out.append("NO")
            continue
        ans = [0] * n
        cnt = 1
        for i in range(n):
            if s[i] == '1':
                ans[i] = cnt
                cnt += 1
        for i in range(n):
            if ans[i] == 0:
                ans[i] = cnt
                cnt += 1         
        out.append("YES")
        out.append(" ".join(map(str, ans)))
    print("\n".join(out))
if __name__ == '__main__':
    main()
