def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        # 시간복잡도 고려
        # 제곱수의 약수의 개수는 항상 홀수
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i
    return answer
