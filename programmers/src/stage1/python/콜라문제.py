def solution(a, b, n):
    answer = 0
    # 더이상 교환하지 못할 때까지
    while n // a != 0:
        answer += (n // a) * b
        n += (n // a) * (b - a)
    return answer
