def solution(n):
    # 정수를 문자열 리스트로
    li = list(str(n))
    # 정렬, 뒤집기 -> sort(reverse = True) 와 같음.
    li.sort()
    li.reverse()
    # 문자열 리스트 -> 문자열 -> 정수 (join 함수 이용)
    answer = int("".join(li))
    return answer
