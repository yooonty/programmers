def solution(x, n):
    answer = []
    for i in range(n):
        # list에 요소 추가
        answer.append(x * (i + 1))
    return answer
