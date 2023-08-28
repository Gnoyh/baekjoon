# https://www.acmicpc.net/problem/11005

N, B = map(int, input().split())

check_int = N

result = ""

while True:
    if check_int % B >= 10:
        result = chr(check_int % B + 55) + result
    else:
        result = str(check_int % B) + result

    if check_int // B == 0:
        break
    else:
        check_int = check_int // B

print(result)