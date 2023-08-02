def solution(s):
    # 문자열 내 특정 문자 갯수 세기 -> count 이용
    # lower 이용 가능
    p = s.count("p") + s.count("P")
    y = s.count("y") + s.count("Y")
    answer = True if p == y else False
    return answer
