def solution(arr, divisor):
    answer = []
    for i in arr:
        # 나누어 떨어질 때 요소 추가
        if i % divisor == 0:
            answer.append(i)
    # 정렬 or [-1]
    answer.sort() if len(answer) != 0 else answer.append(-1)
    return answer
