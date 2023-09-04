def solution(k, score):
    answer = []
    # 임시 저장소
    tmp = []

    for i in score:
        tmp.append(i)
        tmp.sort()
        # 임시 저장소의 개수가 k보다 작을때
        if len(tmp) < k:
            answer.append(tmp[0])
        else:
            answer.append(tmp[-k])
    return answer
