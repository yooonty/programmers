def solution(n):
    answer = 0
    for i in range(1, n + 1):
        # i가 약수일 경우
        if n % i == 0:
            answer += i
    return answer
