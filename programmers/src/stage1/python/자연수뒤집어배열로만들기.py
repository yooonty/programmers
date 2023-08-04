def solution(n):
    # 각 자릿수를 list로 변환하고 reverse
    answer = list(map(int, str(n)))
    answer.reverse()
    return answer
