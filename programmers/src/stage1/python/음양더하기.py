def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        # 부호에 따라 +/-
        answer = answer + absolutes[i] if signs[i] else answer - absolutes[i]
    return answer
