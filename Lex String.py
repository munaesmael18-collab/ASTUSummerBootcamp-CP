import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        k = int(data[idx+2])
        
        a = list(data[idx+3])
        b = list(data[idx+4])
        idx += 5
        a.sort()
        b.sort()
        
        c = []
        i, j = 0, 0
        count_a, count_b = 0, 0
        while i < n and j < m:
            if count_a == k:
                c.append(b[j])
                j += 1
                count_b = 1
                count_a = 0
            elif count_b == k:
                c.append(a[i])
                i += 1
                count_a = 1
                count_b = 0
            else:
                if a[i] < b[j]:
                    c.append(a[i])
                    i += 1
                    count_a += 1
                    count_b = 0  
                else:
                    c.append(b[j])
                    j += 1
                    count_b += 1
                    count_a = 0 
                    
        out.append("".join(c))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
