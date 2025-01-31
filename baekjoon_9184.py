# https://www.acmicpc.net/problem/9184

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif w_list[a][b][c] != 1:
        return w_list[a][b][c]
    elif a < b and b < c:
        w_list[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        
        return w_list[a][b][c]
    else:
        w_list[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        
        return w_list[a][b][c]
        

while True:
    w_list = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]
    
    a, b, c = input().split()
    
    a = int(a)
    b = int(b)
    c = int(c)
    
    if a == b == c == -1:
        break
    else:
        result = w(a, b, c)
        
        print(f"w({a}, {b}, {c}) = {result}")