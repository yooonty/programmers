import math


def solution(n):
    # 제곱/제곱근 구하기 -> math.pow/math.sqrt 이용
    r = int(math.sqrt(n))
    answer = math.pow(r + 1, 2) if n == math.pow(r, 2) else -1
    return answer
