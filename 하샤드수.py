def solution(x):
    li = list(map(int, str(x)))
    # 각 자릿수의 합 sum 함수 이용
    answer = True if x % sum(li) == 0 else False
    return answer
