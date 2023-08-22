def solution(food):
    o = ""
    for i in range(1, len(food)):
        o += str(i) * int(food[i] / 2)

    # 문자열 뒤집기 -> 문자열[::-1]
    answer = o + "0" + o[::-1]
    return answer
