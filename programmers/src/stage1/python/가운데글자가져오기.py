def solution(s):
    # s길이의 절반
    m = int(len(s) / 2)
    return s[m] if len(s) % 2 != 0 else s[m - 1 : m + 1]
