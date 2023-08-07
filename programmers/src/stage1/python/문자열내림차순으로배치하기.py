def solution(s):
    # 문자열을 list로
    answer = list(s)
    # list를 내림차순으로 정렬
    answer.sort(reverse=True)
    # list를 문자열로 - join 함수 이용
    return "".join(answer)
