def solution(n):
    # 각 자릿수를 list로 변환
    answer = list(map(int, str(n)))
    return sum(answer)
