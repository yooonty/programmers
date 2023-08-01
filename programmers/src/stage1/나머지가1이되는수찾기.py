def solution(n):
    answer = 0
    for i in range(1, n + 1):
        # 나머지가 1이 되는 가장 작은 자연수 찾고 반복문 break
        if n % i == 1:
            answer = i
            break
    return answer
