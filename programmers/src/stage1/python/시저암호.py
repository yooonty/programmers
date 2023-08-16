def solution(s, n):
    answer = ""
    # ord()/chr() 이용
    for i in s:
        # 대문자일 때
        if i.isupper():
            answer += chr((ord(i) - ord("A") + n) % 26 + ord("A"))
        # 소문자일 때
        elif i.islower():
            answer += chr((ord(i) - ord("a") + n) % 26 + ord("a"))
        # 공백일 때
        else:
            answer += " "
    return answer
