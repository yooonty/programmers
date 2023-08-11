def solution(s):
    answer = ""
    # 단어의 index를 저장
    idx = 0
    for i in s:
        # 공백일 때
        if i == " ":
            answer += i
            idx = 0

        # 공백이 아닐 때
        else:
            # 단어의 index가 짝수
            if idx % 2 == 0:
                answer += i.upper()
            # 단어의 index가 홀수
            else:
                answer += i.lower()
            idx += 1
    return answer
