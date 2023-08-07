def solution(a, b):
    # zip 함수 이용
    answer = [i * j for i, j in zip(a, b)]
    return sum(answer)
