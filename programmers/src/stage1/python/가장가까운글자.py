def solution(s):
    # 문자의 가장 마지막 인덱스를 담을 딕셔너리
    dic = {}
    answer = []

    for i in range(len(s)):
        # 딕셔너리 안에 문자가 있을 때
        if s[i] in dic:
            answer.append(i - dic[s[i]])
        # 딕셔너리 안에 문자가 없을 때
        else:
            answer.append(-1)
        dic[s[i]] = i
    return answer
