def solution(n):
    # 뒤집은 3진수를 저장할 문자열
    result = ""
    while n:
        result += str(n % 3)
        n = n // 3

    # int(str,진법) => 10진법으로 출력
    answer = int(result, 3)
    return answer
