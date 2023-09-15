def solution(k, m, score):
    # score 내림차순 정렬
    score.sort(reverse=True)
    # 과일상자 판매금
    answer = 0
    for i in range(len(score) // m):
        start = m * i
        answer += min(score[start : start + m]) * m
    return answer
