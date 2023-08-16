def solution(t, p):
    answer = 0
    # t에서 p와 길이가 같은 부분문자열 개수
    l = len(t) - len(p) + 1
    for i in range(l):
        if t[i : i + len(p)] <= p:
            answer += 1
    return answer
