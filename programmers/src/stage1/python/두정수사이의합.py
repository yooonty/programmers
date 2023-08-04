def solution(a, b):
    answer = 0
    # sum 함수 이용 가능
    for i in range(min(a, b), max(a, b) + 1):
        answer += i
    return answer
