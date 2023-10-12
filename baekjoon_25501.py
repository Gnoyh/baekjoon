# https://www.acmicpc.net/problem/25501

from sys import stdin

T = int(stdin.readline())

def recursion(s, l, r, check_recur):
    check_recur += 1

    if l >= r:
        return [1, check_recur]
    elif s[l] != s[r]:
        return [0, check_recur]
    else:
        return recursion(s, l + 1, r - 1, check_recur)

def isPalindrome(s):
    return recursion(s, 0, len(s) - 1, 0)

def return_count():
    for _ in range(T):
        input_str = stdin.readline().rstrip()

        print(isPalindrome(input_str)[0], end=" ")
        print(isPalindrome(input_str)[1])

return_count()